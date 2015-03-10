import time
from jit_compile import JIT
from sympy.abc import x

NExpr = 10

f_exprs = []
for i in range(1,NExpr):
	expr = reduce(lambda a, b:a+b, [x**(1.0/(j+1)) for j in range(0,i)])
	f_exprs.append(expr)
	print expr

ts = time.time()
g1 = map(lambda a:JIT().compile([x], a), f_exprs)
te = time.time()
print g1
print "LLVM JIT compile time: ",(te-ts)
print "LLVM JIT eval value= "
for g in g1:
	print g(0.1)

N=10000000
for g in g1:
	ts = time.time()
	for j in range(N):
		g(0.1)
	te = time.time()
	print "LLVM JIT time: ", (te-ts)

