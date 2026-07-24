def approve(customer):
    return {
        "decision": "APPROVE",
        "reason": "Low risk customer"
    }

def verify(customer):
    return {
        "decision": "VERIFY",
        "questions": [
            "National ID",
            "Last recharge amount",
            "Last 3 called numbers"
        ]
    }

def escalate(customer):
    return {
        "decision": "ESCALATE",
        "reason": "Possible SIM swap fraud"
    }