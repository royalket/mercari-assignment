from pathlib import Path

def get_yaml_files(path):
    path = Path(path).resolve()
    if path.is_file():
        return [path]
    elif path.is_dir():
        return list(path.glob('**/*.yaml')) + list(path.glob('**/*.yml'))
    else:
        raise ValueError(f"Invalid path: {path}")

def get_nested_value(data, key):
    keys = key.split('.')
    for k in keys:
        if isinstance(data, dict):
            data = data.get(k)
        else:
            return None
    return data