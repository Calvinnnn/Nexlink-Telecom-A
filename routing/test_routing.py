#!/usr/bin/env python3
import sys
import json
import os

# Change to parent directory so relative imports work
os.chdir('/home/calvin/Desktop/Nexlink-Telecom-A/Nexlink-Telecom-A')
sys.path.insert(0, 'shared')

from router import route
from tools import load_accounts, check_account_history, check_recent_activity, check_device_reputation, check_sim_swap_history

def infer_risk(acc):
    age = acc.get("account_age_days", 0)
    device_new = acc.get("device_new", False)
    location_changed = acc.get("location_changed", False)
    sim_swaps = acc.get("recent_sim_swaps", 0)
    if sim_swaps > 2:
        return "HIGH_RISK"
    if age < 120 and (device_new or location_changed):
        return "HIGH_RISK"
    if device_new and location_changed:
        return "MEDIUM_RISK"
    if device_new or location_changed:
        return "MEDIUM_RISK"
    return "LOW_RISK"

accounts = load_accounts()
print("=" * 80)
print("ROUTING ARCHITECTURE TEST - All Accounts")
print("=" * 80)
for acc_id in sorted(accounts.keys()):
    acc = accounts[acc_id]
    risk = infer_risk(acc)
    decision = route(risk, acc)
    print(f"\n{acc_id}: {risk} -> {decision['decision']}")
    if acc_id == "acc_005":
        print("  LIMITATION: Cannot reconsider after initial classification")
