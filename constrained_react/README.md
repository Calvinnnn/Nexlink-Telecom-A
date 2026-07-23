# Constrained ReAct Agent

## How to Run
From the project root folder:

```bash
pip install google-genai python-dotenv pydantic
python constrained_react/main.py
```

Make sure a `.env` file exists in the project root with your API key

## Model / Provider
- Provider: Google AI Studio (Gemini API)
- Model: `gemini-flash-latest` (alias, points to Google's current stable
  Flash model)
  - You can change this, but after trying a few model names that turned out
    to be deprecated or unavailable to new users, this was the only one that
    worked during development.

## What Makes This "Constrained"
- **Validation schema**: `schema.py` defines `AgentStep` using Pydantic,
  restricting the `action` field to a fixed set of allowed values.
- **Tool allow-list**: `ALLOWED_ACTIONS` in `schema.py`.
- **MAX_STEPS**: set to `6` in `main.py`.
- The loop must end in either a `final_answer` action, or an automatic
  `ESCALATE` if `MAX_STEPS` is reached or validation repeatedly fails.