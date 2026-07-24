from enum import Enum

class Decision(Enum):
    APPROVE = "APPROVE"
    VERIFY = "VERIFY"
    ESCALATE = "ESCALATE"
    REJECT = "REJECT"