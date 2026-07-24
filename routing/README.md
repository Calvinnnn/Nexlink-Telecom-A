**Idea of routing**
Instead of writing 200 rules, we have the LLM classify the case as:

LOW_RISK

Medium Risk

High Risk

Then, we revert to standard code.


**work flow**
Deterministic Routing

Customer request → LLM classification → Fixed handler → Final decision