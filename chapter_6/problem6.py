# Complete the above implementation of json_encode by handling the case of dictionaries.
import json
def json_encode(data):
    if isinstance(data, dict):
	return json.dumps(data)
    

