import math
def fac(n):
	a, i = 1, 2
	while i <= n:
		a, i= a*i, i+1 
	return a
def zeros(n):
	s, k = 0, int(math.log(n,5))
	for i in xrange(1,n+1):		
		
		s, i = s+int(n/(5**i)), i+1
	return s		
n = 10
print str(zeros(n))+ ' zeros at the end'
print str(n)+'!='+str(fac(n))