import json
def has_complex_structure(json_str):
    try:
        data = json.loads(json_str)
        def is_complex(value):
            if isinstance(value, dict):
                return any(isinstance(v, (dict, list)) for v in value.values())
            elif isinstance(value, list):
                return any(isinstance(i, (dict, list)) for i in value)
            return False
        return is_complex(data)
    except json.JSONDecodeError:
        return False
# Example Usage
json_str1 = '{"product": "laptop", "specs": {"cpu": "i7", "ram": "16GB"}}'
json_str2 = '{"product": "laptop", "price": 1500}'
print(has_complex_structure(json_str1))  # True (contains a nested dictionary)
print(has_complex_structure(json_str2))  # False (simple flat structure)
# OUTPUT:
# True
# False
