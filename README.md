<img src="./header.svg" width="100%" alt="Tanishq Dhawan. Full-stack developer, AI agents, open source." />

I build full-stack apps and the AI agents that live inside them. TypeScript and Python, schema to UI, and I care most about the boring parts that make software trustworthy: money stored as `DECIMAL`, claims traced to a source, agents that get fired when they fail.

**Tech Lead** at The Byte Club &nbsp;·&nbsp; **Software lead** at Agnie Racing &nbsp;·&nbsp; [LinkedIn](https://linkedin.com/in/tanishq-dhawan) &nbsp;·&nbsp; [Email](mailto:tanishqdhawan2111@gmail.com)

<br>

<img src="./assets/stats.svg" width="100%" alt="GitHub stats" />

<br>

### Things I've built

<sub>Hardest first. Every card opens the repo.</sub>

<a href="https://github.com/HackToBerFest-VVCE/t2c1-dancing-burgers"><img src="./assets/card-sworn.svg" width="49%" alt="Sworn: 2nd place at HacktoberFest VVCE. Hires AI agents from Solana's agent registries, benchmarks them, and fires the ones that fail." /></a>
<a href="https://github.com/CALL-ME-TATA/FundLens"><img src="./assets/card-fundlens.svg" width="49%" alt="FundLens: mutual fund tracker with real returns and XIRR." /></a>
<a href="https://github.com/CALL-ME-TATA/Retail_Chatbot"><img src="./assets/card-empathiq.svg" width="49%" alt="EmpathIQ: 1st place at the TCS Hackathon. Support bot that reads customer sentiment and escalates to a human." /></a>
<a href="https://github.com/thewalker045/ByteClub2026-V2"><img src="./assets/card-byteclub.svg" width="49%" alt="Byte Club website: the official site for The Byte Club at NIE." /></a>
<a href="https://github.com/CALL-ME-TATA/wattwise"><img src="./assets/card-wattwise.svg" width="49%" alt="WattWise: agents that watch power use, flag anomalies and forecast usage." /></a>
<a href="https://github.com/CALL-ME-TATA/inventory-management-mern"><img src="./assets/card-inventory.svg" width="49%" alt="Inventory: MERN inventory with products, variants, sales and purchases." /></a>

<details>
<summary><b>How they work</b> &nbsp;<sub>click to expand</sub></summary>
<br>

**Sworn** &nbsp;<sub>2nd place, HacktoberFest VVCE, Track 2, with team Dancing Burgers. I wrote most of the commits.</sub>
- Screens every agent the same way: independent on-chain reputation, a liveness check, then a benchmark on SQuAD 2.0, HotpotQA and FEVER
- LangGraph pipeline where every claim carries its source and is checked by a different agent; a dead agent is swapped out mid-run
- Writes each agent's performance back on-chain, sealed with a SHA-256 hash of the evidence, and flags fake ratings (self-ratings, rings, bursts)
- MCP server, Prometheus metrics, CI on GitHub Actions, all in Docker Compose

**FundLens** &nbsp;<sub>in progress</sub>
- XIRR from a hand-written Newton-Raphson solver that falls back to bisection, with tests
- Money lives in PostgreSQL as `DECIMAL`, never float, and every write is a transaction
- A daily cron job pulls NAVs from mfapi.in (AMFI data) with idempotent upserts; Express API with JWT auth; React and Recharts dashboard

**EmpathIQ** &nbsp;<sub>1st place, TCS Hackathon, with Team Knight CODERS. <a href="https://retail-chatbot-two.vercel.app">Try it live</a></sub>
- LangGraph flow: detect sentiment, decide whether to keep going or escalate, reply without inventing policy
- RoBERTa sentiment at 97.2% accuracy on held-out retail chats; also fine-tuned DistilBERT on Amazon reviews to compare
- Answers grounded in a TF-IDF knowledge base, Gemini with fallbacks, template replies if no LLM is reachable

**Byte Club website**
- Next.js frontend and an Express backend on Supabase, with Resend for email. One of the main contributors, 30 commits

**WattWise**
- Separate Google ADK agents for ingestion, anomaly detection, forecasting and reporting, over time-series energy data through an async pipeline

**Inventory**
- Auth, search, filters and pagination across products, sellers, sales and purchases; Zod validation on both ends, Redux Toolkit on the client

</details>

<br>

### Open source

**[Kestra](https://github.com/kestra-io/kestra)** &nbsp;two fixes to the open-source workflow orchestrator, in Java
- [#21356](https://github.com/kestra-io/kestra/pull/21356) &nbsp;Upper-case Pebble function arguments and secret keys with `Locale.ROOT`, so `secret('api_key')` stops looking up `APİ_KEY` on Turkish machines
- [#21951](https://github.com/kestra-io/kestra/pull/21951) &nbsp;Re-enable `SecretFunctionTest.getSecret` and migrate its flow to `fromJson`

**[Open Source BYTE 2K26](https://byteopensource.github.io/)** &nbsp;a beginner open source program I help run at The Byte Club, where students land their first PR on the site itself. 29 commits

<br>

### Stack

<img src="./assets/stack.svg" width="100%" alt="Stack: TypeScript, React, Next.js, Node.js, Express, Python, FastAPI, PostgreSQL, MongoDB, Redis, LangGraph, Docker and more." />

<br>

### Activity

<img src="./assets/activity.svg" width="100%" alt="Contribution graph for the last year" />

<sub>Stats and graph refresh daily from the GitHub API through a small Action in this repo.</sub>
