#sage benchmark
#load("benchmark-sage-rosenbrock.py")
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

#Gradient
grad = []
for x in xs:
	grad.append(rosen.diff(x))
for e in grad:
	print e

fV = []
fV.append(fast_float(grad[0], *xs[0:2]))
for i in range(1,N-1):
	args = xs[i-1:i+2];
	#print args, "=>", grad[i]
	fV.append(fast_float(grad[i], *args))
fV.append(fast_float(grad[-1], *xs[-2:]))

args2 = [1.0, 1.0]
args = [1.0, 1.0, 1.0]
print fV[0](*args2)
for i in range(1,N-1):
	print fV[i](*args)
print fV[-1](*args2)

out = 0.0;
NN=100000
ts = time.time()
for i in range(NN):
	args2[0] += 1e-15
	args2[1] += 1e-15
	args[0] += 1e-15
	args[1] += 1e-15
	args[2] += 1e-15
	out += fV[0](*args2)
	for i in range(1,N-1):
		out += fV[i](*args)
	out += fV[-1](*args2)
te = time.time()
print "sage grad time: ", (te-ts)
print "Final Value=", out