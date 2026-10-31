<img src="./header.svg" width="100%" alt="Tanishq Dhawan. Full-stack developer, AI agents, open source." />

I'm a full-stack developer and a third-year Information Science student at NIE Mysuru. I build web apps end to end in TypeScript and Python, from the database schema to the UI, and lately a lot of AI agents that work with messy real-world data.

Outside coursework I'm the Tech Lead at The Byte Club, and I lead software for Agnie Racing, our college EV motorsport team.

<br>

<img src="./assets/stack.svg" width="100%" alt="Stack: TypeScript, React, Next.js, Node.js, Express, Python, FastAPI, PostgreSQL, MongoDB, Redis, LangGraph, Docker and more." />

<br>

**Projects** &nbsp;<sub>ordered by complexity: moving parts, scope, and how hard it was to get right</sub>

<details>
<summary><img src="./assets/complexity-5.svg" height="12" alt="Complexity 5 of 5" /> &nbsp;<a href="https://github.com/HackToBerFest-VVCE/t2c1-dancing-burgers"><b>Sworn</b></a> &nbsp;<b>2nd place, HacktoberFest VVCE.</b> Hires AI agents from Solana's open agent registries and keeps only the ones that prove themselves.</summary>
<br>

- Screens every agent the same way: independent on-chain reputation, a liveness check, then a benchmark on SQuAD 2.0, HotpotQA and FEVER
- LangGraph pipeline where every claim carries its source and is checked by a different agent; a dead agent is swapped out mid-run
- Writes each agent's performance back on-chain, sealed with a SHA-256 hash of the evidence
- Flags fake ratings on the registry: self-ratings, rings, bursts
- MCP server, Prometheus metrics, CI on GitHub Actions, all in Docker Compose
- Built with team Dancing Burgers. I wrote most of the commits

`Python` `FastAPI` `LangGraph` `Next.js` `Solana` `PostgreSQL` `Redis` `MCP` `Docker`
</details>

<details>
<summary><img src="./assets/complexity-4.svg" height="12" alt="Complexity 4 of 5" /> &nbsp;<a href="https://github.com/CALL-ME-TATA/FundLens"><b>FundLens</b></a> &nbsp;A mutual fund tracker that turns SIP, lump-sum and redemption history into real returns and XIRR. <i>In progress.</i></summary>
<br>

- XIRR from a hand-written Newton-Raphson solver that falls back to bisection, with tests
- Money lives in PostgreSQL as `DECIMAL`, never float, and every write is a transaction
- A daily cron job pulls NAVs from mfapi.in (AMFI data) with idempotent upserts
- Express API with JWT auth, React dashboard with value over time and allocation by category

`TypeScript` `Node` `Express` `PostgreSQL` `React` `Docker`
</details>

<details>
<summary><img src="./assets/complexity-4.svg" height="12" alt="Complexity 4 of 5" /> &nbsp;<a href="https://github.com/CALL-ME-TATA/Retail_Chatbot"><b>EmpathIQ</b></a> &nbsp;A retail support bot that reads how a customer feels and knows when to hand off to a human.</summary>
<br>

- LangGraph flow: detect sentiment, decide whether to keep going or escalate, reply without inventing policy
- RoBERTa sentiment at 97.2% accuracy on held-out retail chats; also fine-tuned DistilBERT on Amazon reviews to compare
- Answers grounded in a TF-IDF knowledge base, Gemini with fallbacks, template replies if no LLM is reachable
- Built with Team Knight CODERS for the TCS Hackathon. [Try it live](https://retail-chatbot-two.vercel.app)

`Python` `FastAPI` `LangGraph` `PyTorch` `Transformers` `React`
</details>

<details>
<summary><img src="./assets/complexity-3.svg" height="12" alt="Complexity 3 of 5" /> &nbsp;<a href="https://github.com/thewalker045/ByteClub2026-V2"><b>Byte Club website</b></a> &nbsp;The official site for The Byte Club at NIE.</summary>
<br>

- Next.js frontend and an Express backend on Supabase, with Resend for email
- One of the main contributors, 30 commits

`Next.js` `TypeScript` `Express` `Supabase`
</details>

<details>
<summary><img src="./assets/complexity-3.svg" height="12" alt="Complexity 3 of 5" /> &nbsp;<a href="https://github.com/CALL-ME-TATA/wattwise"><b>WattWise</b></a> &nbsp;Agents on Google ADK that watch power consumption, flag anomalies and forecast usage.</summary>
<br>

- Separate agents for ingestion, anomaly detection, forecasting and reporting
- Works over time-series energy data from several sources, through an async pipeline

`Python` `Google ADK` `LLM agents`
</details>

<details>
<summary><img src="./assets/complexity-2.svg" height="12" alt="Complexity 2 of 5" /> &nbsp;<a href="https://github.com/CALL-ME-TATA/inventory-management-mern"><b>Inventory</b></a> &nbsp;A MERN inventory system with products, variants, sales and purchases.</summary>
<br>

- Auth, search, filters and pagination across products, sellers, sales and purchases
- Zod validation on both ends, Redux Toolkit on the client

`TypeScript` `React` `Express` `MongoDB`
</details>

<br>

**Open source**

<details>
<summary><a href="https://github.com/kestra-io/kestra"><b>Kestra</b></a> &nbsp;Two fixes to the open-source workflow orchestrator, in Java.</summary>
<br>

- [#21356](https://github.com/kestra-io/kestra/pull/21356) &nbsp;Upper-case Pebble function arguments and secret keys with `Locale.ROOT`, so they don't break on locales like Turkish
- [#21951](https://github.com/kestra-io/kestra/pull/21951) &nbsp;Re-enable `SecretFunctionTest.getSecret` and migrate its flow to `fromJson`
</details>

<details>
<summary><a href="https://github.com/byteopensource/byteopensource.github.io"><b>Open Source BYTE 2K26</b></a> &nbsp;A beginner open source program I help run, where students land their first PR on the site itself.</summary>
<br>

- Students add a contributor file, open a PR, and level up from there to real projects
- 29 commits to the program site. [See it live](https://byteopensource.github.io/)
</details>

<br>

**Activity**

<img src="./assets/stats.svg" width="100%" alt="GitHub stats" />

<br>

<img src="./assets/activity.svg" width="100%" alt="Contribution graph for the last year" />

<sub>Both refresh daily from the GitHub API through a small Action in this repo.</sub>

<br><br>

[LinkedIn](https://linkedin.com/in/tanishq-dhawan) &nbsp;·&nbsp; [Email](mailto:tanishqdhawan2111@gmail.com)
