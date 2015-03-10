# Use Gauss-Newton algorithm to fit a given model
# See http://en.wikipedia.org/wiki/Gauss-Newton_algorithm
from sympy import *
from sympy.abc import *
from jit_compile import JIT
from ctypes import *

def Gauss_Newton(eq, data_dict, init_params_dict, eps=1e-4, max_iter=100):
	J = [] #Jacobian in a list (rowwise)
	rs = [] #residuals
	dlen = 0 #length of measurement data
	for key, val in data_dict.items():
		dlen = len(val)
		break

	params_tuple = tuple(init_params_dict.keys())
	nparams = len(params_tuple)
	for idx in range(dlen):
		#Substitute x,y,... with their data of measurement
		r = data_dict[eq.lhs][idx] - eq.rhs
		for var in data_dict:
			r = r.subs(var, data_dict[var][idx])

		for idx in range(nparams):
			J.append(r.diff(params_tuple[idx]))
		rs.append(r)
	#print J
	#print rs

	funcJ = JIT().compile2(params_tuple, J)
	len_J = len(J)
	funcRs = JIT().compile2(params_tuple, rs)
	len_rs = len(rs)

	init_vals = []
	for idx in range(nparams):
		init_vals.append(init_params_dict[params_tuple[idx]])
	
	for it in range(max_iter):
		outAryJ = (c_double*len_J)()
		funcJ(*tuple(init_vals + [byref(outAryJ)]))
		outAryRs = (c_double*len_rs)()
		funcRs(*tuple(init_vals+[byref(outAryRs)]))

		NJ = [] #Jacobian matrix, dim: (nRow,nCol)=(dlen, nparams)
		for row in range(dlen):
			NJrow = []
			for col in range(nparams):
				NJrow.append(outAryJ[row*nparams+col])
			NJ.append(NJrow)
		A = Matrix(NJ)

		Nrs = []
		for row in range(dlen):
			Nrs.append(outAryRs[row])
		bb = Matrix(Nrs)

		Ab = (A.T*A).row_join(A.T*bb)
		sol = solve_linear_system(Ab, *params_tuple)
		norm = 0
		for idx in range(nparams):
			upd = sol[params_tuple[idx]]
			init_vals[idx] = init_vals[idx] - upd
			norm = norm + upd*upd
		if sqrt(norm) < eps:
			#print "Number of iteratons: %d" % it
			break

	ret = {}
	for idx in range(nparams):
		ret[params_tuple[idx]] = init_vals[idx]
	return ret


sol = Gauss_Newton(
	Eq(y,a*x/(b+x)), 
	{
		x:[0.038,0.194,0.425,0.626,1.253,2.500,3.740],
		y:[0.050,0.127,0.094,0.2122,0.2729,0.2665,0.3317]
	},
	{ a: 0.9, b: 0.2 } 
)
print sol

