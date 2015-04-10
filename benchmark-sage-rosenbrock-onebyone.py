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
print "Sage fast_float onebyone"
print "N|gradCompileTime|Grad Eval Time|Grad CheckSum"

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

	fV = []
	ts = time.time()
	fV.append(fast_float(grad[0], *xs[0:2]))
	for i in range(1,N-1):
		args = xs[i-1:i+2];
		#print args, "=>", grad[i]
		fV.append(fast_float(grad[i], *args))
	fV.append(fast_float(grad[-1], *xs[-2:]))
	te = time.time()
	gradCompileTime = te-ts

	args2 = [1.0, 1.0]
	args = [1.0, 1.0, 1.0]
	if debug:
		print fV[0](*args2)
		for i in range(1,N-1):
			print fV[i](*args)
		print fV[-1](*args2)

	NN = 10000 #*****************************
	gradCheckSum = 0.0;
	xx = 1.0
	ts = time.time()
	for i in range(NN):
		xx += 1e-15
		args2[0] = xx
		xx += 1e-15
		args2[1] = xx
		gradCheckSum += fV[0](*args2)

		for i in range(1,N-1):
			#xx += 1e-15
			args[0] = xx
			#xx += 1e-15
			args[1] = xx
			xx += 1e-15
			args[2] = xx
			gradCheckSum += fV[i](*args)

		#xx += 1e-15
		args2[0] = xx
		#xx += 1e-15
		args2[1] = xx
		gradCheckSum += fV[-1](*args2)
	te = time.time()
	gradEvalTime = te-ts

	print N,gradCompileTime,gradEvalTime,gradCheckSum

	N+=50