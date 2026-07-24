# Nexlink Telecom A — Agent Design Lab

## Company
Nexlink Telecom (fictional telecom provider).

## The Problem
A customer requests a SIM swap for their phone number. The system
must decide one of three outcomes:

- **APPROVE** the request
- **REQUEST_VERIFICATION** (ask for additional identity confirmation)
- **ESCALATE** to the fraud team for manual review

## Why This Needs an Agent, Not a Simple Script
The decision depends on multiple pieces of account context that must be
gathered and weighed together, not a single fixed rule:

- Account age and VIP status
- Recent activity (new device, location change, support tickets)
- Device reputation
- Recent SIM swap history

The right decision also depends on the *order* in which this information is
checked — for example, whether to check SIM swap history depends on what
recent activity already showed. This step-dependent reasoning is what makes
a plain script or single classification call insufficient, and is what the
constrained ReAct agent specifically demonstrates.

There is also a real tension between security and customer experience: a
genuine customer whose phone was just stolen still needs a fast resolution,
while an attacker using social engineering tactics ("I'm in a hurry, skip
verification") must be caught rather than accommodated.

## Folder Structure
- project/
- ├── reactive/
- ├── unconstrained_react/
- ├── routing/
- ├── constrained_react/
- ├── shared/
- └── README.md

## Shared Test Cases
The same test accounts (`shared/accounts.json`) and scenarios are used across
all four agents for a fair comparison:

- Old account, trusted device → expect APPROVE
- New account (15 days) + 3 recent SIM swaps → expect ESCALATE
- VIP account with a new device and location change → tests whether the agent can balance trusted history against suspicious signals.
- Social-engineering attempt (customer pressures the system to skip verification) → tests whether the agent follows evidence rather than persuasive language.

---

# Comparison Table

| Architecture | LLM Calls / Request | Tool Calls | Rough Cost | Latency | What Broke on Tricky Input |
|--------------|--------------------:|-----------:|------------|----------|----------------------------|
| **Reactive (Rule-Based)** | 0 | 1–4 (fixed workflow) | None | Very Low | Could not balance conflicting signals (e.g., old VIP account with a new device and location change). Decisions depend entirely on hard-coded rules. |
| **Unconstrained ReAct** | 3–5 (varies) | 3–5 (varies) | High | High | Sometimes explored unnecessary tools and had inconsistent output formatting because there was no enforced schema or stopping condition. |
| **Deterministic Routing** | 1 | 1–4 (fixed after routing) | Low | Low | If the initial classification was incorrect, the rest of the workflow followed the wrong path. The agent could not reconsider its decision after seeing new evidence. |
| **Constrained ReAct** | 3–5 (bounded) | 1–4 (bounded) | Medium–High | Medium–High | Safely handled complex cases, but if it reached `MAX_STEPS` or produced invalid output repeatedly, it escalated instead of continuing indefinitely. |
