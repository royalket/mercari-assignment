import argparse
from yaml_parser import parse_yaml_files
from rule_checker import check_rules

def main():
    parser = argparse.ArgumentParser(description="Kubernetes YAML Linter")
    parser.add_argument("path", help="Path to YAML file or directory")
    parser.add_argument("key", help="Key to search for in YAML")
    parser.add_argument("value", help="Value to match against the key")
    parser.add_argument("--regex", action="store_true", help="Use regex matching")
    args = parser.parse_args()

    yaml_data = parse_yaml_files(args.path)
    results = check_rules(yaml_data, args.key, args.value, use_regex=args.regex)

    for result in results:
        print(f"key = {result['key']}, value = {result['value']}, {result['file']}")

if __name__ == "__main__":
    main()