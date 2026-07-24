import sys
import json
import os

# Change to parent directory so relative imports work
os.chdir('/home/calvin/Desktop/Nexlink-Telecom-A/Nexlink-Telecom-A')
sys.path.insert(0, 'shared')

from router import route
from tools import load_accounts, check_account_history, check_recent_activity, check_device_reputation, check_sim_swap_history


ARCHITECTURAL_NOTES = {
    "acc_001": "LOW_RISK expected: old account (400d), trusted device, no activity. Should APPROVE. ✓ No limitation",
    "acc_002": "HIGH_RISK expected: new account (15d) + 3 SIM swaps + suspicious activity. Should ESCALATE. ✓ Correctly caught",
    "acc_003": "MEDIUM/HIGH_RISK: VIP + new device + location_changed + old account (900d). LIMITATION: Router cannot weight VIP status or reconsider after initial classification.",
    "acc_004": "MEDIUM_RISK expected: new device only but account age 200d, location stable. Should VERIFY. No limitation",
    "acc_005": "⚠️ ROUTING LIMITATION CASE: New account (20d) + device_new + location_changed, BUT clean history (0 SIM swaps, trusted device). Router will classify as HIGH_RISK and ESCALATE immediately. A multi-step agent could ask 'Did you upgrade your phone?' and accept the explanation. Router cannot reconsider.",
}


def run_all_accounts():
    """Load all accounts from accounts.json and run routing for each."""
    accounts = load_accounts()
    
    print("=" * 80)
    print("ROUTING ARCHITECTURE TEST")
    print("=" * 80)
    print()
    
    for account_id, account_data in sorted(accounts.items()):
        print(f"\n{'─' * 80}")
        print(f"ACCOUNT: {account_id}")
        print(f"{'─' * 80}")
        
        
        history = check_account_history(account_id)
        activity = check_recent_activity(account_id)
        device_rep = check_device_reputation(account_id)
        sim_swaps = check_sim_swap_history(account_id)
        
        print(f"Account History: {json.dumps(history, indent=2)}")
        print(f"Recent Activity: {json.dumps(activity, indent=2)}")
        print(f"Device Reputation: {device_rep}")
        print(f"SIM Swap History: {sim_swaps}")
        print()
        
        
        risk_label = infer_risk_label(account_data, account_id)
        print(f"Inferred Risk Label: {risk_label}")
        
        
        result = route(risk_label, account_data)
        print(f"Router Decision: {json.dumps(result, indent=2)}")
        
        
        print(f"\nArchitectural Note: {ARCHITECTURAL_NOTES.get(account_id, 'N/A')}")


def infer_risk_label(account, account_id):
    """
    Simulate the classifier's logic based on the account data.
    This is a simplified version without LLM calls.
    """
    account_age = account.get("account_age_days", 0)
    device_new = account.get("device_new", False)
    location_changed = account.get("location_changed", False)
    sim_swaps = account.get("recent_sim_swaps", 0)
    is_vip = account.get("is_vip", False)
    
    if sim_swaps > 2:
        return "HIGH_RISK"
    
    if account_age < 120 and (device_new or location_changed):
        return "HIGH_RISK"
    
    if device_new and location_changed:
        return "MEDIUM_RISK"
    
    if device_new:
        return "MEDIUM_RISK"
    
    if location_changed:
        return "MEDIUM_RISK"
    
    return "LOW_RISK"

if __name__ == "__main__":
    run_all_accounts()
