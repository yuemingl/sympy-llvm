import time
import theano.tensor as T
from theano import function
from sympy.printing.theanocode import theano_function
from math import factorial

print __file__

NExpr = 10

x = T.dvector('x')

f_exprs = []
for i in range(0,NExpr):
	expr = reduce(lambda a, b:a+b, [1.0/factorial(j)*x**j for j in range(0,i+1)])
	f_exprs.append(expr)
	print expr

ts = time.time()
g1 = map(lambda a:function([x], a), f_exprs)
te = time.time()
print g1
print "theano function compile time: ",(te-ts)
print "theano theano_function eval value="
for g in g1:	
	print g([0.1])	


ts = time.time()
g2 = map(lambda a:theano_function([x], [a], dims={x: 1}, dtypes={x: 'float64'}), f_exprs)
te = time.time()
print g2
print "sympy.printing.theanocode theano_function compile time: ",(te-ts)
print "sympy.printing.theanocode theano_function eval value="
for g in g2:	
	print g([0.1])	

nData = 10000 #the best one
NN=10000000
N=NN/nData
print "Total loops:",N
aryX = [0.1 for i in range(nData)]

for i in range(len(f_exprs)):
	ts = time.time()
	for j in range(N):
		r = g1[i](aryX)
	te = time.time()
	#print r
	print "theano function time: ",(te-ts), " expr=", f_exprs[i] 


for i in range(len(f_exprs)):
	ts = time.time()
	for j in range(N):
		g2[i](aryX)
	te = time.time()
	print "sympy.printing.theanocode theano_function time: ",(te-ts), " expr=", f_exprs[i] 