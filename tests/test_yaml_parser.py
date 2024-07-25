import unittest
from pathlib import Path
from src.yaml_parser import parse_yaml_files

class TestYamlParser(unittest.TestCase):
    def test_parse_single_yaml(self):
        test_file = Path(__file__).parent.parent / 'example_yamls' / 'example_1.yaml'
        result = parse_yaml_files(test_file)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['content']['apiVersion'], 'apps/v1')

    def test_parse_multiple_yamls(self):
        test_dir = Path(__file__).parent.parent / 'example_yamls'
        result = parse_yaml_files(test_dir)
        self.assertGreater(len(result), 1)

if __name__ == '__main__':
    unittest.main()