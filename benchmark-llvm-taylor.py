import time
from jit_compile import JIT
from sympy import *
from sympy.abc import x
#from math import factorial

print __file__

NExpr = 10

f_exprs = []
for i in range(0,NExpr):
	expr = reduce(lambda a, b:a+b, [1.0/factorial(j)*x**j for j in range(0,i+1)])
	f_exprs.append(expr)
	print expr

ts = time.time()
g1 = map(lambda a:JIT().Compile([x], a), f_exprs)
te = time.time()
print g1
print "LLVM JIT compile time: ",(te-ts)
#print "LLVM JIT eval value= "
#for g in g1:
#	print g(0.1)

N=10000000
xx = 0.1
out = 0.0
for i in range(len(g1)):
	ts = time.time()
	for j in range(N):
		g1[i](xx)
	te = time.time()
	print "Without changing param time=", (te-ts), " expr=", f_exprs[i] 

for i in range(len(g1)):
	ts = time.time()
	for j in range(N):
		xx += 1e-15
		out += g1[i](xx)
	te = time.time()
	print "With changing param time=", (te-ts), " expr=", f_exprs[i] 
print "Final Value=", out
