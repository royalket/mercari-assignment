import yaml
from pathlib import Path

def parse_yaml_files(path):
    path = Path(path)
    parsed_yamls = []

    if path.is_file():
        parsed_yamls.extend(parse_single_file(path))
    elif path.is_dir():
        for yaml_file in path.glob('**/*.yaml'):
            parsed_yamls.extend(parse_single_file(yaml_file))

    return parsed_yamls

def parse_single_file(file_path):
    parsed_docs = []
    with open(file_path, 'r') as file:
        try:
            docs = yaml.safe_load_all(file)
            for doc in docs:
                if doc:  # Skip empty documents
                    parsed_docs.append({
                        'content': doc,
                        'file_path': str(file_path)
                    })
        except yaml.YAMLError as e:
            print(f"Error parsing {file_path}: {e}")
    return parsed_docs