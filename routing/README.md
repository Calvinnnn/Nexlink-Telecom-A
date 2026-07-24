**Idea of routing**
Instead of writing 200 rules, we have the LLM classify the case as:

LOW_RISK

Medium Risk

High Risk

Then, we revert to standard code.


**work flow**
Deterministic Routing

Customer request → LLM classification → Fixed handler → Final decision



**why it's better than my first arch reactive?**


Because an LLM can aggregate signals.

For example:

Changing devices

Changing governorates

Having a wallet

Requesting a replacement

Any single one of these might not be enough on its own, but together, they indicate high risk.


**when does it fail**

The "Murder" Scenario

The caller says:

"I am in Cairo, but the phone is available in Cairo because my brother has it."

The model might classify this as:

High Risk

or Medium Risk

However, the router cannot change its mind after new information emerges.


**failing example**
The Fatal Scenario

The customer says:

“I am in Cairo, but the phone is still active in Alexandria because my brother has it.”

The model might classify this as:

HIGH_RISK

or MEDIUM_RISK

However, the router cannot change its decision once new information emerges.


Reactive

“We chose the rule-based agent first because it was the cheapest and fastest to build. It performed well on obvious fraud patterns, but it failed whenever the customer’s intent had to be inferred from language or multiple weak signals.”

Routing

“The deterministic routing agent added one LLM classification step, which improved flexibility and reduced the number of hard-coded rules. However, it still could not conduct a multi-step investigation or revise its decision after receiving new evidence."

## Running routing

From the `routing/` directory, run:

```bash
cd /home/calvin/Desktop/Nexlink-Telecom-A/Nexlink-Telecom-A/routing
python run_routing.py LOW_RISK
```

You can also choose a different sample customer:

```bash
python run_routing.py HIGH_RISK --customer-id acc_002
```

Or provide a custom customer JSON:

```bash
python run_routing.py MEDIUM_RISK --customer-json /path/to/customer.json
```
