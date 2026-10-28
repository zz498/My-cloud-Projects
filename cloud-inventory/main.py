"""Explore a sample cloud inventory using Python's standard library."""

import argparse
import json
from pathlib import Path


RESOURCE_FILE = Path(__file__).with_name("resources.json")


def load_resources(file_path=RESOURCE_FILE):
    """Load resource records from a JSON file."""
    with file_path.open(encoding="utf-8") as resource_file:
        return json.load(resource_file)


def get_resources(resources, environment=None):
    """Return all resources, optionally filtered by environment."""
    if environment is None:
        return resources
    return [resource for resource in resources if resource["environment"] == environment]


def total_monthly_cost(resources):
    """Add the estimated monthly costs of a collection of resources."""
    return sum(resource["monthly_cost"] for resource in resources)


def print_resources(resources):
    if not resources:
        print("No resources found.")
        return

    print(f"{'NAME':<20} {'TYPE':<18} {'ENVIRONMENT':<14} {'MONTHLY COST':>13}")
    print("-" * 69)
    for resource in resources:
        print(
            f"{resource['name']:<20} {resource['type']:<18} "
            f"{resource['environment']:<14} ${resource['monthly_cost']:>11.2f}"
        )


def print_summary(resources):
    if not resources:
        print("No resources found.")
        return

    environments = sorted({resource["environment"] for resource in resources})
    print(f"Resources: {len(resources)}")
    print(f"Estimated monthly total: ${total_monthly_cost(resources):.2f}")
    print("Cost by environment:")
    for environment in environments:
        matching_resources = get_resources(resources, environment)
        print(f"  {environment}: ${total_monthly_cost(matching_resources):.2f}")


def build_parser():
    parser = argparse.ArgumentParser(description="Explore a sample cloud resource inventory.")
    commands = parser.add_subparsers(dest="command")

    list_command = commands.add_parser("list", help="List resources")
    list_command.add_argument("--environment", help="Only show this environment")
    commands.add_parser("summary", help="Show estimated monthly costs")
    parser.set_defaults(command="list", environment=None)
    return parser


def main():
    args = build_parser().parse_args()
    resources = load_resources()

    if args.command == "list":
        print_resources(get_resources(resources, args.environment))
    else:
        print_summary(resources)


if __name__ == "__main__":
    main()
