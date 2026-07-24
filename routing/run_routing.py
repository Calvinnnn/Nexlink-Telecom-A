import argparse
import json

from router import route

SAMPLE_CUSTOMERS = {
    "acc_001": {
        "account_id": "acc_001",
        "device_id": "dev-A",
        "current_location": "home",
        "wallet_present": False,
        "wallet_location": None,
        "action": "RECHARGE"
    },
    "acc_002": {
        "account_id": "acc_002",
        "device_id": "dev-C",
        "current_location": "country_A",
        "wallet_present": True,
        "wallet_location": "country_B",
        "action": "PORT_OUT"
    }
}


def main():
    parser = argparse.ArgumentParser(
        description="Run routing handlers for a sample customer"
    )
    parser.add_argument(
        "label",
        nargs="?",
        choices=["LOW_RISK", "MEDIUM_RISK", "HIGH_RISK"],
        default="LOW_RISK",
        help="Risk label to pass to routing.router.route",
    )
    parser.add_argument(
        "--customer-id",
        default="acc_001",
        help="Sample customer ID to use from SAMPLE_CUSTOMERS",
    )
    parser.add_argument(
        "--customer-json",
        help="Path to a JSON file containing customer data",
    )
    args = parser.parse_args()

    if args.customer_json:
        with open(args.customer_json, "r") as f:
            customer = json.load(f)
    else:
        customer = SAMPLE_CUSTOMERS.get(args.customer_id)
        if customer is None:
            raise ValueError(f"Unknown sample customer id: {args.customer_id}")

    result = route(args.label, customer)
    print("Route label:", args.label)
    print("Customer:")
    print(json.dumps(customer, indent=2))
    print("Result:")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
