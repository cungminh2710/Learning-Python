def prime(n):
	result = range(2,n)
	loop = 0
	for i, val in enumerate(result):
		for j in range(2,val):
			loop = loop + 1
			if not val % j:
				result[i]=None
				break
	print 'Prime takes '+str(loop) + ' loops\n'	
	return result

def prime1(n):
	result = range(2, n)
	loop = 0
	for j in range(2, n):
		temp = j
		while temp+j<n:
			loop = loop+1
			temp = temp + j
			result[temp - 2] = None
	print 'Prime1 takes '+str(loop) + ' loops\n'
	return result

n = 30000
if prime(n) == prime1(n):
	print 'Same results\n'