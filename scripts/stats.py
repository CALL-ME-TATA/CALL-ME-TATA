"""Builds the animated SVGs on the profile README.

Run by .github/workflows/stats.yml every day. Needs GITHUB_TOKEN (the Actions token is enough).
`python scripts/stats.py --demo` renders with fake data, no network, for checking the look locally.
"""
import json
import os
import random
import sys
import urllib.request
from datetime import date, datetime, timedelta, timezone
from html import escape

LOGIN = os.environ.get("LOGIN", "CALL-ME-TATA")
OUT = os.path.join(os.path.dirname(__file__), "..", "assets")

# Edit this to change the stack section.
STACK = [
    ("Frontend", ["TypeScript", "React", "Next.js", "Tailwind", "Redux"]),
    ("Backend", ["Node.js", "Express", "Python", "FastAPI", "REST", "JWT"]),
    ("Data", ["PostgreSQL", "MongoDB", "Redis", "Supabase"]),
    ("AI", ["LangGraph", "Google ADK", "LLM agents", "MCP"]),
    ("Infra", ["Docker", "GitHub Actions", "Vercel", "Linux", "Solana"]),
]

# Same palette as header.svg, light first, then dark.
STYLE = """
    :root { --fg: #1f2328; --muted: #656d76; --line: #d0d7de; --accent: #0969da; --empty: #ebedf0; --chip: #f6f8fa; }
    @media (prefers-color-scheme: dark) {
      :root { --fg: #e6edf3; --muted: #8d96a0; --line: #30363d; --accent: #4493f8; --empty: #161b22; --chip: #161b22; }
    }
    text { font-family: ui-sans-serif, -apple-system, "Segoe UI", Helvetica, Arial, sans-serif; }
    .mono { font-family: ui-monospace, SFMono-Regular, "Cascadia Code", Consolas, monospace; }
    @keyframes fade { from { opacity: 0; } to { opacity: 1; } }
    @keyframes up { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: none; } }
    @keyframes grow { from { transform: scaleX(0); } to { transform: scaleX(1); } }
    @keyframes pop { from { opacity: 0; transform: scale(.3); } to { opacity: 1; transform: scale(1); } }
"""


def svg(w, h, label, body, extra_style=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{escape(label)}">\n<style>{STYLE}{extra_style}</style>\n{body}\n</svg>\n')


# ---------- data ----------

QUERY = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    createdAt
    pullRequests { totalCount }
    merged: pullRequests(states: MERGED) { totalCount }
    repositoriesContributedTo(contributionTypes: [COMMIT, PULL_REQUEST], includeUserRepositories: false) { totalCount }
    contributionsCollection(from: $from, to: $to) {
      totalCommitContributions
      restrictedContributionsCount
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount contributionLevel } }
      }
    }
  }
}"""

LEVELS = {"NONE": 0, "FIRST_QUARTILE": 1, "SECOND_QUARTILE": 2, "THIRD_QUARTILE": 3, "FOURTH_QUARTILE": 4}


def gql(token, frm, to):
    body = json.dumps({"query": QUERY, "variables": {"login": LOGIN, "from": frm.isoformat(), "to": to.isoformat()}})
    req = urllib.request.Request("https://api.github.com/graphql", body.encode(),
                                 {"Authorization": f"bearer {token}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    if data.get("errors"):
        sys.exit(f"GraphQL error: {data['errors']}")
    return data["data"]["user"]


def fetch(token):
    now = datetime.now(timezone.utc)
    # The API caps each query at one year, so walk back a year at a time to the account's creation.
    first = gql(token, now - timedelta(days=365), now)
    created = datetime.fromisoformat(first["createdAt"].replace("Z", "+00:00"))
    windows, commits, days = [first], 0, {}
    to = now - timedelta(days=365)
    while to > created:
        windows.append(gql(token, max(created, to - timedelta(days=365)), to))
        to -= timedelta(days=365)
    for w in windows:
        cc = w["contributionsCollection"]
        commits += cc["totalCommitContributions"] + cc["restrictedContributionsCount"]
        for wk in cc["contributionCalendar"]["weeks"]:
            for d in wk["contributionDays"]:
                days[d["date"]] = d["contributionCount"]
    last_year = [[(d["date"], d["contributionCount"], LEVELS[d["contributionLevel"]]) for d in wk["contributionDays"]]
                 for wk in first["contributionsCollection"]["contributionCalendar"]["weeks"]]
    return {
        "commits": commits,
        "prs": first["pullRequests"]["totalCount"],
        "merged": first["merged"]["totalCount"],
        "repos": first["repositoriesContributedTo"]["totalCount"],
        "year_total": first["contributionsCollection"]["contributionCalendar"]["totalContributions"],
        "weeks": last_year,
        **streaks(days),
    }


def streaks(days):
    """Current and longest run of days with at least one contribution. Today not counting yet doesn't break it."""
    if not days:
        return {"current": 0, "longest": 0}
    d, end = date.fromisoformat(min(days)), date.fromisoformat(max(days))
    longest = run = 0
    while d <= end:
        run = run + 1 if days.get(d.isoformat(), 0) else 0
        longest = max(longest, run)
        d += timedelta(days=1)
    d = end if days.get(end.isoformat(), 0) else end - timedelta(days=1)
    current = 0
    while days.get(d.isoformat(), 0):
        current += 1
        d -= timedelta(days=1)
    return {"current": current, "longest": longest}


def demo():
    # streak sanity checks: a quiet today keeps yesterday's run alive, a gap resets it
    assert streaks({"2026-01-01": 1, "2026-01-02": 2, "2026-01-03": 0}) == {"current": 2, "longest": 2}
    assert streaks({"2026-01-01": 1, "2026-01-02": 0, "2026-01-03": 1, "2026-01-04": 1}) == {"current": 2, "longest": 2}
    assert streaks({"2026-01-01": 1, "2026-01-02": 0, "2026-01-03": 0}) == {"current": 0, "longest": 1}
    random.seed(4)
    start = date.today() - timedelta(days=364 + (date.today().weekday() + 1) % 7)
    weeks, days = [], {}
    for w in range(53):
        week = []
        for i in range(7):
            d = start + timedelta(days=w * 7 + i)
            if d > date.today():
                break
            c = random.choice([0, 0, 0, 1, 2, 3, 5, 8, 12]) if w > 20 else random.choice([0, 0, 0, 0, 1, 2])
            days[d.isoformat()] = c
            week.append((d.isoformat(), c, 0 if not c else min(4, 1 + c // 3)))
        weeks.append(week)
    return {"commits": 412, "prs": 9, "merged": 6, "repos": 5, "year_total": sum(days.values()),
            "weeks": weeks, **streaks(days)}


# ---------- render ----------

def stats_svg(s):
    items = [
        (f"{s['commits']:,}", "commits, all time"),
        (f"{s['year_total']:,}", "contributions this year"),
        (str(s["prs"]), f"pull requests, {s['merged']} merged" if s["merged"] else "pull requests opened"),
        (str(s["repos"]), "repos contributed to"),
        (f"{s['current']}d", "current streak"),
        (f"{s['longest']}d", "longest streak"),
    ]
    col, body = 140, ['<line x1="0" y1="0.5" x2="840" y2="0.5" stroke="var(--line)"/>']
    for i, (num, label) in enumerate(items):
        x, t = i * col, 0.15 + i * 0.12
        body.append(
            f'<rect x="{x}" y="0" width="28" height="2" fill="var(--accent)" '
            f'style="transform-box: fill-box; transform-origin: left; transform: scaleX(0); animation: grow .5s ease-out {t:.2f}s forwards"/>'
            f'<g style="opacity: 0; animation: up .6s ease-out {t + .1:.2f}s forwards">'
            f'<text x="{x}" y="46" fill="var(--fg)" font-size="30" font-weight="600" letter-spacing="-0.5">{escape(num)}</text>'
            f'<text x="{x}" y="70" fill="var(--muted)" font-size="12.5">{escape(label)}</text></g>')
    return svg(840, 84, "GitHub stats: " + ", ".join(f"{n} {l}" for n, l in items), "\n".join(body))


def activity_svg(s):
    cell, gap, top = 11, 3, 18
    pitch = cell + gap
    body, last_month = [], None
    for w, week in enumerate(s["weeks"]):
        for d, count, level in week:
            dt = date.fromisoformat(d)
            if dt.day <= 7 and dt.month != last_month and w < len(s["weeks"]) - 1:
                last_month = dt.month
                body.append(f'<text class="m" x="{w * pitch}" y="11">{dt.strftime("%b")}</text>')
            fill = "var(--empty)" if level == 0 else "var(--accent)"
            op = ["1", ".3", ".5", ".75", "1"][level]
            body.append(
                f'<rect x="{w * pitch}" y="{top + dt.isoweekday() % 7 * pitch}" width="{cell}" height="{cell}" rx="2" '
                f'fill="{fill}" fill-opacity="{op}" style="animation-delay: {w * 0.022:.3f}s">'
                f'<title>{count} on {d}</title></rect>')
    y = top + 7 * pitch + 20
    width = len(s["weeks"]) * pitch
    body.append(f'<text class="m" x="0" y="{y}">{s["year_total"]:,} contributions in the last year</text>')
    lx = width - 5 * pitch - 70
    body.append(f'<text class="m" x="{lx}" y="{y}">Less</text>')
    for i, op in enumerate(["1", ".3", ".5", ".75", "1"]):
        fill = "var(--empty)" if i == 0 else "var(--accent)"
        body.append(f'<rect class="k" x="{lx + 32 + i * pitch}" y="{y - 10}" width="{cell}" height="{cell}" rx="2" '
                    f'fill="{fill}" fill-opacity="{op}"/>')
    body.append(f'<text class="m" x="{lx + 32 + 5 * pitch + 4}" y="{y}">More</text>')
    style = """
    .m { fill: var(--muted); font-size: 11px; opacity: 0; animation: fade .6s ease-out .2s forwards; }
    rect { opacity: 0; transform-box: fill-box; transform-origin: center; animation: pop .35s ease-out forwards; }
    rect.k { animation-delay: 1.2s; }
    """
    return svg(width, y + 6, f"{s['year_total']} contributions in the last year", "\n".join(body), style)


def stack_svg():
    char, pad, h, gapx, rowh, labelw = 7.6, 12, 26, 8, 40, 96
    body = []
    for r, (group, items) in enumerate(STACK):
        y, t = r * rowh, 0.1 + r * 0.15
        body.append(f'<text x="0" y="{y + 17}" fill="var(--muted)" font-size="12.5" '
                    f'style="opacity: 0; animation: fade .5s ease-out {t:.2f}s forwards">{group}</text>')
        x = labelw
        for i, item in enumerate(items):
            w = round(len(item) * char + pad * 2)
            body.append(
                f'<g style="opacity: 0; animation: up .45s ease-out {t + 0.06 * (i + 1):.2f}s forwards">'
                f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="var(--chip)" stroke="var(--line)"/>'
                f'<text class="mono" x="{x + w / 2}" y="{y + 17}" text-anchor="middle" fill="var(--fg)" font-size="12.5">'
                f'{escape(item)}</text></g>')
            x += w + gapx
    return svg(840, len(STACK) * rowh - 14, "Stack: " + "; ".join(f"{g}: {', '.join(i)}" for g, i in STACK),
               "\n".join(body))


def meter_svg(n):
    """Five bars, n of them lit, filling left to right. Used as the complexity rating next to each project."""
    body = []
    for i in range(5):
        lit = i < n
        body.append(
            f'<rect x="{i * 9}" y="1" width="7" height="10" rx="1.5" fill="{"var(--accent)" if lit else "var(--empty)"}"'
            + (f' style="opacity: 0; animation: fade .3s ease-out {0.3 + i * 0.12:.2f}s forwards"' if lit else "")
            + "/>")
    return svg(44, 12, f"Complexity {n} of 5", "".join(body))


def write(name, text):
    with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def main():
    os.makedirs(OUT, exist_ok=True)
    if "--demo" in sys.argv:
        s = demo()
    else:
        token = os.environ.get("GITHUB_TOKEN") or sys.exit("GITHUB_TOKEN is not set")
        s = fetch(token)
    write("stats.svg", stats_svg(s))
    write("activity.svg", activity_svg(s))
    write("stack.svg", stack_svg())
    for n in range(1, 6):
        write(f"complexity-{n}.svg", meter_svg(n))
    print(json.dumps({k: v for k, v in s.items() if k != "weeks"}))


if __name__ == "__main__":
    main()
