import time
from jit_compile import JIT
from sympy import *
from sympy.abc import x
#from math import factorial

print __file__

NExpr = 10

f_exprs = []
for i in range(1,NExpr):
	expr = reduce(lambda a, b:a+b, [1.0/factorial(j)*x**j for j in range(0,i)])
	f_exprs.append(expr)
	print expr

ts = time.time()
g1 = map(lambda a:JIT().Compile([x], a), f_exprs)
te = time.time()
print g1
print "LLVM JIT compile time: ",(te-ts)
print "LLVM JIT eval value= "
for g in g1:
	print g(0.1)

N=10000000
for i in range(len(g1)):
	ts = time.time()
	for j in range(N):
		g1[i](0.1)
	te = time.time()
	print "LLVM JIT time: ", (te-ts), " expr=", f_exprs[i] 

