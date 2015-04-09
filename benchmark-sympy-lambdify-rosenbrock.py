import time

import ctypes
from sympy import *
from sympy.abc import x

from sympy.utilities.autowrap import ufuncify #not work
from sympy.utilities.lambdify import lambdify

print __file__

debug = false

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

	v_grad = Matrix(grad)
	f_grad = lambdify(xs, v_grad);

	vlen = len(xs)
	args = []
	for i in range(len(xs)):
		args.append(1.0)
	#print f_grad(*args)

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
	f_hess = lambdify(xs, m_hess)
	#print f_hess(*args)

	out = 0.0
	NN=100000
	ts = time.time()
	for i in range(NN):
		for j in range(N):
			args[j] += 1e-15
		outs = f_grad(*args)
		#print outs
		for row in range(N):
			out += outs[row,0]
	te = time.time()
	print "N=",N," sympy grad time: ", (te-ts)

	ts = time.time()
	for i in range(NN):
		for j in range(N):
			args[j] += 1e-15
		outs = f_hess(*args)
		#print outs
		for row in range(N):
			out += outs[row,row]
	te = time.time()
	print "N=",N," sympy hess time: ", (te-ts)

	print "Final Value=", out

	N += 50