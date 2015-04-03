import time
from jit_compile import JIT
from sympy import *
from ctypes import *
from sympy.core.numbers import Zero

print __file__



N = 20
xs = symbols('x1:%d'%(N+1))
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

func_grad = JIT().BatchCompile(xs, grad)

vlen = len(xs)
outAry = (c_double*vlen)()
args = []
for i in range(len(xs)):
	args.append(0.0)

func_grad(*( args + [byref(outAry)] ))

for d in outAry:
	print d, 

#Hessian Matrix
hess = []
for g in grad:
	tmp = []
	for x in xs:
		tmp.append(g.diff(x))
	hess.append(tmp)


hess_list = reduce(lambda x,y: x+y, hess)
#print hess_list
func_hess = JIT().BatchCompile(xs, hess_list)

vlen = len(xs)*len(xs)
outAry = (c_double*vlen)()
args = []
for i in range(len(xs)):
	args.append(0.0)
func_hess(*( args + [byref(outAry)] ))

for d in outAry:
	print d, 