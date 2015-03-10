import time
import theano.tensor as T
from theano import function
from sympy.printing.theanocode import theano_function

NExpr = 10

x = T.dscalar('x')

f_exprs = []
for i in range(1,NExpr):
	expr = reduce(lambda a, b:a+b, [x**(1.0/(j+1)) for j in range(0,i)])
	f_exprs.append(expr)
	print expr

ts = time.time()
g1 = map(lambda a:function([x], a), f_exprs)
te = time.time()
print g1
print "theano function compile time: ",(te-ts)
print "theano theano_function eval value="
for g in g1:	
	print g(0.1)	


ts = time.time()
g2 = map(lambda a:theano_function([x], [a], dims={x: 1}, dtypes={x: 'float64'}), f_exprs)
te = time.time()
print g2
print "theano theano_function compile time: ",(te-ts)
print "theano theano_function eval value="
for g in g2:	
	print g(0.1)	


N=10000000
print "Total loops:",N

for i in range(len(f_exprs)):
	ts = time.time()
	for j in range(N):
		g1[i](0.1)
	te = time.time()
	print "theano function time: ",(te-ts)


for i in range(len(f_exprs)):
	ts = time.time()
	for j in range(N):
		g1[i](0.1)
	te = time.time()
	print "theano theano_function time: ",(te-ts)