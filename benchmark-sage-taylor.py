#Sage benchmark
#load("benchmark-sage-taylor.py")
import time

NExpr = 10
x = var('x')

f_exprs = []
for i in range(0,NExpr):
	expr = exp(x).taylor(x, 0, i)
	f_exprs.append(expr)
	print expr

ts = time.time()
g1 = map(lambda a:fast_float(a, x), f_exprs)
te = time.time()
print g1
print "sage fast_float compile time: ",(te-ts)
for g in g1:
	print g.op_list()
print "sage fast_float eval value= "
for g in g1:
	print g(0.1)

N=10000000
print "benchmark:"
for i in range(len(f_exprs)):
	ts = time.time()
	for j in range(N):
		g1[i](0.1)
	te = time.time()
	print "sage fast_float time: ", (te-ts), " expr=", f_exprs[i] 
