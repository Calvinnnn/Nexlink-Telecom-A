import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from shared.tools import (
    check_account_history,
    check_recent_activity,
    check_device_reputation,
    check_sim_swap_history,
    request_additional_verification,
    escalate_to_fraud_team
)

# Configuration constants
MIN_ACCOUNT_AGE = 30
MIN_SUPPORT_TICKETS = 2
MAX_SIM_SWAPS = 3

def decide(account_id):

    # Rule 1: Very new accounts are considered high risk.
    history = check_account_history(account_id)
    if history["account_age_days"] < MIN_ACCOUNT_AGE:
        escalate_to_fraud_team(account_id)
        return "ESCALATE"

    # Rule 2: Multiple recent SIM swaps indicate possible fraud.
    swap_count = check_sim_swap_history(account_id)
    if swap_count >= MAX_SIM_SWAPS:
        escalate_to_fraud_team(account_id)
        return "ESCALATE"

    # Rule 3: A new device combined with a location change is suspicious.
    activity = check_recent_activity(account_id)
    if activity["device_new"] and activity["location_changed"]:
        escalate_to_fraud_team(account_id)
        return "ESCALATE"

    # Rule 4: Unknown devices or many support tickets require verification.
    device_rep = check_device_reputation(account_id)
    if activity["recent_support_tickets"] > MIN_SUPPORT_TICKETS or device_rep == "unknown":
        request_additional_verification(account_id)
        return "REQUEST_VERIFICATION"

    return "APPROVE"


if __name__ == "__main__":
    test_accounts = ["acc_001", "acc_002", "acc_003", "acc_004"]
    for acc in test_accounts:
        result = decide(acc)
        print(f"{acc} -> {result}\n")