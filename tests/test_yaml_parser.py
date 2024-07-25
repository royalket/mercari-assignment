import unittest
from src.yaml_parser import parse_yaml_files

class TestYamlParser(unittest.TestCase):
    def test_parse_single_yaml(self):
        result = parse_yaml_files('example_yamls/example_1.yaml')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['content']['apiVersion'], 'apps/v1')

    def test_parse_multiple_yamls(self):
        result = parse_yaml_files('example_yamls')
        self.assertGreater(len(result), 1)

if __name__ == '__main__':
    unittest.main()