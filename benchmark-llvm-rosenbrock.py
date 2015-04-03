import time
from jit_compile import JIT
from sympy import *
from ctypes import *
from sympy.core.numbers import Zero

print __file__

debug = false

NTest = 300

for N in range(10,NTest):

	xs = symbols('x1:%d'%(N+1))
	if debug:
		print xs

	rosen = 0
	for i in range(1,N):
		rosen += 100*(xs[i]-xs[i-1]**2)**2 + (1-xs[i-1])**2
	if debug:
		print rosen

	#Gradient
	grad = []
	for x in xs:
		grad.append(rosen.diff(x))
	if debug:
		for e in grad:
			print e

	ts = time.time()
	func_grad = JIT().BatchCompile(xs, grad)
	te = time.time()
	#print "llvm rosen grad (N=",N,") compile time: ",(te-ts)


	vlen = len(xs)
	outAry = (c_double*vlen)()
	args = []
	for i in range(len(xs)):
		args.append(0.0)

	func_grad(*( args + [byref(outAry)] ))

	if debug:
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
	ts = time.time()
	func_hess = JIT().BatchCompile(xs, hess_list)
	te = time.time()
	print "llvm rosen hess (N=",N,") compile time: ",(te-ts)

	vlen = len(xs)*len(xs)
	outAry = (c_double*vlen)()
	args = []
	for i in range(len(xs)):
		args.append(0.0)
	func_hess(*( args + [byref(outAry)] ))

	if debug:
		for d in outAry:
			print d, 

#llvm rosen grad (N= 300 ) compile time:  5.63664889336
#llvm rosen hess (N= 300 ) compile time:  278.574788094		