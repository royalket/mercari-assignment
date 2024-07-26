from .utils import get_nested_value

def check_rules(yaml_data, key, value):
    results = []

    for doc in yaml_data:
        content = doc['content']
        file_path = doc['file_path']

        if '[*]' in key:
            base_key, list_key = key.split('[*]')
            list_values = get_nested_value(content, base_key)
            if isinstance(list_values, list):
                for i, item in enumerate(list_values):
                    item_value = get_nested_value(item, list_key.lstrip('.'))
                    if check_value(item_value, value):
                        results.append({
                            'key': f"{base_key}[{i}]{list_key}",
                            'value': item_value,
                            'file': file_path
                        })
        else:
            actual_value = get_nested_value(content, key)
            if check_value(actual_value, value):
                results.append({
                    'key': key,
                    'value': actual_value,
                    'file': file_path
                })

    return results

def check_value(actual_value, expected_value):
    if actual_value is None:
        return False
    try:
        return int(actual_value) == int(expected_value)
    except ValueError:
        return str(actual_value) == str(expected_value)