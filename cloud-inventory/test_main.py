import unittest

from main import build_parser, get_resources, total_monthly_cost


class InventoryTests(unittest.TestCase):
    def setUp(self):
        self.resources = [
            {"name": "app", "environment": "production", "monthly_cost": 25.0},
            {"name": "db", "environment": "development", "monthly_cost": 10.0},
        ]

    def test_filters_resources_by_environment(self):
        result = get_resources(self.resources, "production")
        self.assertEqual([resource["name"] for resource in result], ["app"])

    def test_returns_all_resources_without_filter(self):
        self.assertEqual(get_resources(self.resources), self.resources)

    def test_sums_monthly_costs(self):
        self.assertEqual(total_monthly_cost(self.resources), 35.0)

    def test_empty_inventory_cost_is_zero(self):
        self.assertEqual(total_monthly_cost([]), 0)

    def test_list_is_the_default_command(self):
        args = build_parser().parse_args([])
        self.assertEqual(args.command, "list")
        self.assertIsNone(args.environment)


if __name__ == "__main__":
    unittest.main()
