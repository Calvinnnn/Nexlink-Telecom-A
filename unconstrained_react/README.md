# Unconstrained ReAct Agent

This variant is intentionally left unconstrained in the ways shown in your image:

- Unbounded reasoning chains: there is no hard step cap in the loop.
- Unvalidated model output: the agent does not enforce a schema or reject malformed generations.
- No termination guarantee: it keeps running until the model emits a final decision, so a manual stop may be needed.

It still has access to the same shared tools as the constrained agent, but it does not gate the model through the same validation and retry controls.
