# Deterministic Routing Agent

## Overview

This implementation uses a **single LLM classification step** followed by deterministic business logic.

Instead of making the final decision directly, the language model classifies each customer request into one of three predefined risk categories:

- LOW_RISK
- MEDIUM_RISK
- HIGH_RISK

Once the classification is returned, the agent routes the request to a fixed Python handler that performs the corresponding action:

- LOW_RISK → APPROVE
- MEDIUM_RISK → REQUEST_VERIFICATION
- HIGH_RISK → ESCALATE

Only one model call is made per request. All business logic after the classification is implemented using ordinary, testable Python code.

## Limitations

Although the Routing Agent is more flexible than a purely rule-based system, it still has several limitations.

- It performs only one LLM call.
- It cannot ask follow-up questions.
- It cannot use external tools to gather more evidence.
- It cannot perform multi-step reasoning.
- It cannot revise its decision after receiving new information.
- Once a request is classified, the execution path is fixed.

## Model / Provider

- **Model:** Gemini 2.0 Flash
- **Provider:** Google Gemini API

## How to Run

From the project root:

```bash
python routing/main.py
```