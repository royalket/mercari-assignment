import argparse
from pathlib import Path
from .yaml_parser import parse_yaml_files
from .rule_checker import check_rules

def main():
    parser = argparse.ArgumentParser(description="Kubernetes YAML Linter")
    parser.add_argument("path", help="Path to YAML file or directory")
    parser.add_argument("key", help="Key to search for in YAML")
    parser.add_argument("value", help="Value to match against the key")
    args = parser.parse_args()

    path = Path(args.path)
    if path.exists():
        yaml_data = parse_yaml_files(path)
        results = check_rules(yaml_data, args.key, args.value)

        if results:
            for result in results:
                print(f"key = {result['key']}, value = {result['value']}, {result['file']}")
        else:
            print(f"No matching key-value pairs found for key '{args.key}' and value '{args.value}'")
    else:
        print(f"Error: Invalid path '{args.path}'")

if __name__ == "__main__":
    main()