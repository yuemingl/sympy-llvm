import time
import theano.tensor as T
from theano import function
from sympy.printing.theanocode import theano_function
from theano import pp

print __file__

N = 10
xs = []
for i in range(N):
	xs.append(T.dscalar('x%d'%i))
print xs

rosen = 0
for i in range(1,N):
	rosen += 100*(xs[i]-xs[i-1]**2)**2 + (1-xs[i-1])**2
pp(rosen) #???

#Gradient
grad = []
for x in xs:
	grad.append(T.grad(rosen, x))
for e in grad:
	pp(e)


ts = time.time()
bfunc = function(xs, grad)
te = time.time()
print "theano grad compile time: ",(te-ts)
#theano grad compile time:  6.55618715286 (N=20 first time)
#theano grad compile time:  1.12624502182 (N=31)
#theano grad compile time:  20.7800290585 (N=310)

print "theano theano_function eval value="
args = []
for i in range(N):
	args.append(0.0)
print args
print bfunc(*args)	


NN=10000
print "Total loops:",NN

ts = time.time()
for j in range(NN):
	bfunc(*args)
te = time.time()
print "theano function time: ",(te-ts)
