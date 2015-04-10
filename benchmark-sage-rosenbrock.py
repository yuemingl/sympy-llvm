# Sage Benchmark for Rosenbrock
# Use vector and matrix
#
# load("benchmark-sage-rosenbrock.py")
#
import time

#x = var('x')
#M = matrix([[x,x**2],[1/x,x]])
#fM = fast_float(M, x)
#print fM(x=2)

#V = vector([x,x+1,x+2])
#fV=fast_float(V, x)
#print fV(x=2)


N = 105
xs = []
for i in range(N):
	xs.append(var('x%d'%i))
print xs

rosen = 0
for i in range(1,N):
	rosen += 100*(xs[i]-xs[i-1]**2)**2 + (1-xs[i-1])**2
print rosen
fast_float(rosen, *xs)

#Gradient
grad = []
for x in xs:
	grad.append(rosen.diff(x))
for e in grad:
	print e

V = vector(grad)
fV=fast_float(V, *xs)
args = {}
for x in xs:
	args[x] = 1.0
print fV(args)

out = 0.0;
NN=1000
ts = time.time()
for i in range(NN):
	for x in xs:
		args[x] += 1e-15
	outs = fV(args)
	for d in outs:
		out += d
te = time.time()
print "sage grad time: ", (te-ts)
print "Final Value=", out