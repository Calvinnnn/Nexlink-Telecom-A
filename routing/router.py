from handlers import approve, verify, escalate

def route(label, customer):

    if label == "LOW_RISK":
        return approve(customer)

    if label == "MEDIUM_RISK":
        return verify(customer)

    if label == "HIGH_RISK":
        return escalate(customer)

    return escalate(customer)