import yaml
from pathlib import Path
from .utils import get_yaml_files

def parse_yaml_files(path):
    yaml_files = get_yaml_files(path)
    parsed_yamls = []

    for file_path in yaml_files:
        with open(file_path, 'r') as file:
            try:
                docs = yaml.safe_load_all(file)
                for doc in docs:
                    if doc:  # Skip empty documents
                        parsed_yamls.append({
                            'content': doc,
                            'file_path': str(file_path)
                        })
            except yaml.YAMLError as e:
                print(f"Error parsing {file_path}: {e}")

    return parsed_yamls