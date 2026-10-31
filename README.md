<img src="./header.svg" width="100%" alt="Tanishq Dhawan. AI agents, fintech, EV racing software." />

I'm a third-year Information Science student at NIE Mysuru. I write TypeScript and Python, and most of my time goes into two things: AI agents that work with messy real-world data, and finance software where the numbers have to be exactly right.

Outside coursework I lead software for Agnie Racing, our college EV motorsport team, and run the tech side of The Byte Club.

<br>

**Now**

<details>
<summary><a href="https://github.com/CALL-ME-TATA/FundLens">FundLens</a> &nbsp;A mutual fund tracker that turns SIP, lump-sum and redemption history into real returns and XIRR.</summary>
<br>

- XIRR from a hand-written Newton-Raphson solver that falls back to bisection, with tests
- Money lives in PostgreSQL as `DECIMAL`, never float, and every write is a transaction
- A daily cron job pulls NAVs from mfapi.in (AMFI data) with idempotent upserts
- Express API with JWT auth, React dashboard with value over time and allocation by category

`TypeScript` `Node` `Express` `PostgreSQL` `React`
</details>

**Open source**

<details>
<summary><a href="https://github.com/kestra-io/kestra">Kestra</a> &nbsp;Fixes to the open-source workflow orchestrator, in Java.</summary>
<br>

- [#21356](https://github.com/kestra-io/kestra/pull/21356) &nbsp;Upper-case Pebble function arguments and secret keys with `Locale.ROOT`, so they don't break on locales like Turkish
- [#21951](https://github.com/kestra-io/kestra/pull/21951) &nbsp;Re-enable `SecretFunctionTest.getSecret` and migrate its flow to `fromJson`
</details>

**For the club**

<details>
<summary><a href="https://github.com/thewalker045/ByteClub2026-V2">Byte Club website</a> &nbsp;The official site for The Byte Club at NIE.</summary>
<br>

- Next.js frontend and an Express backend on Supabase, with Resend for email
- One of the main contributors, 30 commits

`Next.js` `TypeScript` `Express` `Supabase`
</details>

<details>
<summary><a href="https://github.com/byteopensource/byteopensource.github.io">Open Source BYTE 2K26</a> &nbsp;A beginner open source program where students land their first PR on the site itself.</summary>
<br>

- Students add a contributor file, open a PR, and level up from there to real projects
- [See it live](https://byteopensource.github.io/)
</details>

**Hackathons**

<details>
<summary><a href="https://github.com/HackToBerFest-VVCE/t2c1-dancing-burgers">Sworn</a> &nbsp;Hires AI agents from Solana's open agent registries and keeps only the ones that prove themselves.</summary>
<br>

- Screens every agent the same way: independent on-chain reputation, a liveness check, then a benchmark on SQuAD 2.0, HotpotQA and FEVER
- LangGraph pipeline where every claim carries its source and is checked by a different agent; a dead agent is swapped out mid-run
- Writes each agent's performance back on-chain, sealed with a SHA-256 hash of the evidence
- Also flags fake ratings on the registry: self-ratings, rings, bursts
- Built with team Dancing Burgers for HacktoberFest VVCE, Track 2. I wrote most of the commits

`Python` `FastAPI` `LangGraph` `Next.js` `Solana` `PostgreSQL` `Redis` `MCP`
</details>

<details>
<summary><a href="https://github.com/CALL-ME-TATA/Retail_Chatbot">EmpathIQ</a> &nbsp;A retail support bot that reads how a customer feels and knows when to hand off to a human.</summary>
<br>

- Detects sentiment, decides whether to keep going or escalate, then replies without inventing policy
- Built with Team Knight CODERS for the TCS Hackathon
- [Try it live](https://retail-chatbot-two.vercel.app)
</details>

**Before**

<details>
<summary><a href="https://github.com/CALL-ME-TATA/wattwise">WattWise</a> &nbsp;Agents on Google ADK that watch power consumption, flag anomalies and forecast usage.</summary>
<br>

- Separate agents for ingestion, anomaly detection, forecasting and reporting
- Works over time-series energy data from several sources, through an async pipeline

`Python` `Google ADK` `LLM agents`
</details>

<details>
<summary><a href="https://github.com/CALL-ME-TATA/inventory-management-mern">Inventory</a> &nbsp;A MERN inventory system with products, variants, sales and purchases.</summary>
<br>

- Auth, search, filters and pagination across products, sellers, sales and purchases
- Zod validation on both ends, Redux Toolkit on the client

`TypeScript` `React` `Express` `MongoDB`
</details>

<br>

**Tools** &nbsp;TypeScript, Python, C++, React, Next.js, Node, Express, FastAPI, LangGraph, PostgreSQL, Redis, MongoDB, Solana

<br>

[LinkedIn](https://linkedin.com/in/tanishq-dhawan) &nbsp;·&nbsp; [Email](mailto:tanishqdhawan2111@gmail.com)
