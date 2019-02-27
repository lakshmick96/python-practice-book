#Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.

def flatten_dict(d, base_key=''):
    result = {}
    for key in d.keys():
	if isinstance(d[key], dict):
            result.update(flatten_dict(d[key], base_key = base_key + key + "."))
        else:
            result[base_key + key] = d[key]
    return result
