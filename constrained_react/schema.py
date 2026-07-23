from pydantic import BaseModel
from typing import Literal

# List of allowed actions for the agent
ALLOWED_ACTIONS = [
    "check_account_history",
    "check_recent_activity",
    "check_device_reputation",
    "check_sim_swap_history",
    "final_answer",
]

#agent step schema for validation
class AgentStep(BaseModel):
    thought: str
    action: Literal[
        "check_account_history",
        "check_recent_activity",
        "check_device_reputation",
        "check_sim_swap_history",
        "final_answer",
    ]
    action_input: str
    final_decision: str = ""