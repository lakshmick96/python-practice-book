#Write a function treemap to map a function over nested list

def treemap(fun, l):
	result = []
	for i in l:
		if isinstance(i, list):
			result.append(treemap(fun, i))
		else:
			result.append(fun(i))
	return result
	
