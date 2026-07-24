# Reactive (Rule-Based) Agent

## Overview

This implementation uses a pure rule-based approach with no language model. The agent follows a fixed set of `if/else` rules to decide whether to:

- APPROVE
- REQUEST_VERIFICATION
- ESCALATE

The decision is based on account history, recent activity, device reputation, and SIM swap history.

## Limitations

Because all decisions are hard-coded, the agent cannot reason about conflicting signals or adapt to new scenarios without adding more rules.

## Model / Provider

None (No LLM is used).

## How to Run

From the project root:

```bash
python reactive/main.py
```