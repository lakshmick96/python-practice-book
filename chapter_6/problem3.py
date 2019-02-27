#Write a function unflatten_dict to do reverse of flatten_dict.

def unflatten_dict(d, base_key=''):
	result = {}	
	for k in d.keys():
		if '.' in k:
			base_key, key = k.split('.')
			if base_key in result.keys():
				result[base_key].update(unflatten_dict({key:d[k]}))
			else:
				result.update({base_key: unflatten_dict({key:d[k]})})
		else:
			result.update({k:d[k]})
	return result
			
			
