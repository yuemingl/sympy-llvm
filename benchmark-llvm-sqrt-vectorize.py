import time
from jit_compile import JIT
from sympy.abc import x
from ctypes import *

print __file__

NExpr = 10

f_exprs = []
for i in range(1,NExpr):
	expr = reduce(lambda a, b:a+b, [x**(1.0/(j+1)) for j in range(0,i)])
	f_exprs.append(expr)
	#print expr

vlen = 100
ts = time.time()
g1 = map(lambda a:JIT().VecCompile([x], vlen, [a]), f_exprs)
te = time.time()
time_compile = (te-ts)

outAry = (c_double*vlen)()
pX = (c_double*vlen)()

NN=10000000
N=NN/vlen
xx=0.1
out=0.0
time_compute = 0
for i in range(len(g1)):
	ts = time.time()
	for j in range(N):
		for k in range(vlen):
			xx += 1e-15
			pX[k] = xx
		g1[i](byref(pX), byref(outAry))
		for k in range(vlen):
			out += outAry[k]
	te = time.time()
	time_compute += (te-ts)
	print "Time=", (te-ts), " expr=", f_exprs[i] 
print "Final Value=", out
print "vlen=", vlen, "Time: compile=", time_compile, ",compute=", time_compute, ",total=", (time_compile+time_compute), 

#vlen= 2 Time: compile= 0.0726170539856 ,compute= 58.4039506912 ,total= 58.4765677452
#vlen= 24 Time: compile= 0.111973762512 ,compute= 24.5919082165 ,total= 24.703881979
#vlen= 40 Time: compile= 0.169346094131 ,compute= 23.387018919 ,total= 23.5563650131
#vlen= 80 Time: compile= 0.336376905441 ,compute= 22.0920262337 ,total= 22.4284031391
#vlen= 100 Time: compile= 0.439684867859 ,compute= 22.0058834553 ,total= 22.4455683231
#vlen= 160 Time: compile= 0.863581895828 ,compute= 21.6410160065 ,total= 22.5045979023
#vlen= 200 Time: compile= 1.31426787376 ,compute= 21.7608969212 ,total= 23.0751647949
#vlen= 320 Time: compile= 3.09153103828 ,compute= 22.1314668655 ,total= 25.2229979038

