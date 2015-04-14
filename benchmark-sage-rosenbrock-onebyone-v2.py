# Sage Benchmark for Rosenbrock
# Use fast_float for each expression
#
# load("benchmark-sage-rosenbrock-onebyone.py")
#
import time

#x = var('x')
#M = matrix([[x,x**2],[1/x,x]])
#fM = fast_float(M, x)
#print fM(x=2)

#V = vector([x,x+1,x+2])
#fV=fast_float(V, x)
#print fV(x=2)

debug = False
print "Sage fast_float onebyone v2"
print "N|GradCompileTime|GradEvalTime|HessCompileTime|HessEvalTime|GradCheckSum|HessCheckSum"

N = 5
while N<850:

	xs = []
	for i in range(N):
		xs.append(var('x%d'%i))
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

	f_grad = []
	ts = time.time()
	for g in grad:
		f_grad.append(fast_float(g, *xs))
	te = time.time()
	gradCompileTime = te-ts

	args = []
	for i in range(N):
		args.append(1.0)
	if debug:
		for fg in f_grad:
			print fg(*args)


	hess = []
	index = 0
	for g in grad:
		for x in xs:
			gd = g.diff(x)
			# We need keep the indices for nonzero expressions in Hessian
			if not gd.is_trivial_zero():
				hess.append([gd, index])
			index += 1
	if debug:
		print hess

	f_hess = []
	ts = time.time()
	for h in hess:
		h0 = fast_float(h[0], *xs)
		f_hess.append([h0, h[1]])
	te = time.time()
	hessCompileTime = te-ts

	if debug:
		for fh in f_hess:
			print fh[0](*args)


	NN = 1000 #*****************************
	gradCheckSum = 0.0;
	xx = 1.0
	ts = time.time()
	for i in range(NN):
		for k in range(N):
			xx += 1e-15
			args[k] = xx
		for fg in f_grad:
			gradCheckSum += fg(*args)
	te = time.time()
	gradEvalTime = te-ts


	hessCheckSum = 0.0;
	xx = 1.0
	ts = time.time()
	for i in range(NN):
		for k in range(N):
			xx += 1e-15
			args[k] = xx
		for fh in f_hess:
			#Only sum over diaginal elements
			ret = fh[0](*args)
			if fh[1]%N == fh[1]/N:
				hessCheckSum += ret
	te = time.time()
	hessEvalTime = te-ts

	print N,gradCompileTime,gradEvalTime,hessCompileTime,hessEvalTime,gradCheckSum,hessCheckSum

	N+=50