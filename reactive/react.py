from enum import Enum

class Decision(Enum):
    APPROVE = "APPROVE"
    VERIFY = "VERIFY"
    ESCALATE = "ESCALATE"
    REJECT = "REJECT"


def evaluate(customer):

    
    if customer["wallet"] and not customer["location_match"]:
        return Decision.ESCALATE

    
    if (
        customer["request_type"] == "PORT_OUT"
        and customer["account_age_days"] < 120
    ):
        return Decision.REJECT

    
    if customer["device_changed"]:
        return Decision.VERIFY

    
    if not customer["location_match"]:
        return Decision.VERIFY

    return Decision.APPROVE