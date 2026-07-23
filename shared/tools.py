import json


#load account data from a JSON file (write once use everywhere:)
def load_accounts():
    with open("shared/accounts.json", "r") as f:
        return json.load(f)


#return account history data for the account
def check_account_history(account_id):
    accounts = load_accounts()
    account = accounts.get(account_id)
    return {
        "account_age_days": account["account_age_days"],
        "is_vip": account["is_vip"]
    }


#return recent activity data for the account
def check_recent_activity(account_id):
    accounts = load_accounts()
    account = accounts.get(account_id)
    return {
        "device_new": account["device_new"],
        "location_changed": account["location_changed"],
        "recent_support_tickets": account["recent_support_tickets"]
    }


#check if the device associated with the account has a good reputation
def check_device_reputation(account_id):
    accounts = load_accounts()
    account = accounts.get(account_id)
    return account["device_reputation"]


#check if the account has had any recent SIM swaps
def check_sim_swap_history(account_id):
    accounts = load_accounts()
    account = accounts.get(account_id)
    return account["recent_sim_swaps"]


#record the request in logs
def request_additional_verification(account_id):
    print(f"[ACTION] Verification requested for {account_id}")
    return "VERIFICATION_REQUESTED"


# record the escalation in logs 
def escalate_to_fraud_team(account_id):
    print(f"[ACTION] Escalated to fraud team: {account_id}")
    return "ESCALATED"

