def sum_many(*args):
	result = 0
	for i in args:
		result += i
	return result

print(sum_many(1,2,3))
