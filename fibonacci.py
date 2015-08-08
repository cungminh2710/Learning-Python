def fib(n):
	a, b, loop= 0,1,0 
	while (b < n):
		print b, '\n'
		a,b, loop= b, a+b, loop+1
	print 'fib takes '+str(loop)+' loops',

fib(9223372036854775807)