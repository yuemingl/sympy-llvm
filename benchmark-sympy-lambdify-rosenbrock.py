import time

import ctypes
from sympy import *
from sympy.abc import x

from sympy.utilities.autowrap import ufuncify #not work
from sympy.utilities.lambdify import lambdify

print __file__

debug = false

print "Rosenbrock lambdify(matrix)"
print "N|Grad Compile Time|Grad Eval Time|Hess Compile Time|Hess Eval Time|Grad CheckSum|Hess CheckSum"

N = 5
while N < 850:

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

	#Gradient
	v_grad = Matrix(grad)
	ts = time.time()
	f_grad = lambdify(xs, v_grad);
	te = time.time()
	gradCompileTime = te-ts

	args = []
	for i in range(len(xs)):
		args.append(1.0)
	if debug:
		print f_grad(*args)

	#Hessian Matrix
	hess = []
	for g in grad:
		tmp = []
		for x in xs:
			tmp.append(g.diff(x))
		hess.append(tmp)

	#hess_list = reduce(lambda x,y: x+y, hess)
	#print func_hess(*args)
	m_hess = Matrix(hess)
	ts = time.time()
	f_hess = lambdify(xs, m_hess)
	te = time.time()
	hessCompileTime = te-ts
	if debug:
		print f_hess(*args)

	#Benchmark
	NN = 100 #*********************************
	checkSumGrad = 0.0
	xx = 1.0
	ts = time.time()
	for i in range(NN):
		for j in range(N):
			x += 1e-15
			args[j] = xx
		outs = f_grad(*args)
		for row in range(N):
			checkSumGrad += outs[row,0]
	te = time.time()
	gradEvalTime = te-ts

	checkSumHess = 0.0
	xx = 1.0
	ts = time.time()
	for i in range(NN):
		for j in range(N):
			x += 1e-15
			args[j] = xx
		outs = f_hess(*args)
		for row in range(N):
			checkSumHess += outs[row,row]
	te = time.time()
	hessEvalTime = te-ts

	print N,gradCompileTime,gradEvalTime,hessCompileTime,hessEvalTime,checkSumGrad,checkSumHess
	N += 50