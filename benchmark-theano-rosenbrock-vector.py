#NOT work
import time
import theano.tensor as T
from theano import function
from sympy.printing.theanocode import theano_function
from theano import pp

print __file__

debug = True
print "N|gradCompileTime|gradEvalTime|hessCompileTime|hessEvalTime|FinalValue"

N = 5
while N<850:
	xs = []
	for i in range(N):
		xs.append(T.dvector('x%d'%i))
	if debug:
		print xs

	rosen = 0
	for i in range(1,N):
		rosen += 100*(xs[i]-xs[i-1]**2)**2 + (1-xs[i-1])**2
	if debug:
		pp(rosen) #???

	#Gradient
	grad = []
	for x in xs:
		grad.append(T.grad(rosen, x)) #cost must be a scalar
	if debug:
		for e in grad:
			pp(e) #???

	ts = time.time()
	bfunc = function(xs, grad)
	te = time.time()
	gradCompileTime = te-ts

	args = []
	for i in range(N):
		args.append(1.0)
	if debug:
		print bfunc(*args)

	# hess = []
	# for g in grad:
	# 	tmp = []
	# 	for x in xs:
	# 		tmp.append(T.grad(g, x))
	# 	hess.append(tmp)

	# hess_list = reduce(lambda x,y: x+y, hess)
	# print hess_list
	#theano.gradient.DisconnectedInputError: grad method was asked to compute the gradient with respect to a variable that is not part of the computational graph of the cost, or is used only by a non-differentiable operator: x2


	NN = 100 #*******************************
	out = 0.0
	xx = 1.0

	ts = time.time()
	for j in range(NN):
		for k in range(N):
			xx += 1e-15
			args[k] = xx
		ret = bfunc(*args)
		#print ret
		for k in ret:
			#print k
			out += k
	te = time.time()
	gradEvalTime = te-ts

	print N, gradCompileTime, gradEvalTime, 0, 0, out

	N+=50