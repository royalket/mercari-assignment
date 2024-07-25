import unittest
from src.rule_checker import check_rules

class TestRuleChecker(unittest.TestCase):
    def test_check_simple_rule(self):
        yaml_data = [{'content': {'apiVersion': 'apps/v1'}, 'file_path': 'test.yaml'}]
        result = check_rules(yaml_data, 'apiVersion', 'apps/v1')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['key'], 'apiVersion')
        self.assertEqual(result[0]['value'], 'apps/v1')

    def test_check_nested_rule(self):
        yaml_data = [{'content': {'spec': {'replicas': 3}}, 'file_path': 'test.yaml'}]
        result = check_rules(yaml_data, 'spec.replicas', '3')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['key'], 'spec.replicas')
        self.assertEqual(result[0]['value'], 3)

if __name__ == '__main__':
    unittest.main()