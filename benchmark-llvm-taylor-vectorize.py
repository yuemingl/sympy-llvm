import time
from jit_compile import JIT
from sympy import *
from sympy.abc import x
from ctypes import *

print __file__

NExpr = 10

f_exprs = []
for i in range(1,NExpr):
	expr = reduce(lambda a, b:a+b, [1.0/factorial(j)*x**j for j in range(0,i)])
	f_exprs.append(expr)
	#print expr

vlen = 256
ts = time.time()
g1 = map(lambda a:JIT().VecPtrCompile([x], vlen, [a]), f_exprs)
te = time.time()
time_compile = (te-ts)

outAry = (c_double*vlen)()
pX = (c_double*vlen)()
for i in range(len(pX)):
	pX[i] = 0.1

NN=10000000
N=NN/vlen
time_compute = 0
for i in range(len(g1)):
	ts = time.time()
	for j in range(N):
		g1[i](byref(pX), byref(outAry))
	te = time.time()
	time_compute += (te-ts)
	print "Time=", (te-ts), " expr=", f_exprs[i] 

print "vlen=", vlen, "Time: compile=", time_compile, ",compute=", time_compute, ",total=", (time_compile+time_compute), 

#vlen= 32 Time: compile= 0.0944120883942 ,compute= 2.7474603653 ,total= 2.84187245369
#vlen= 40 Time: compile= 0.106534957886 ,compute= 2.21869874001 ,total= 2.32523369789
#vlen= 64 Time: compile= 0.139792203903 ,compute= 1.55496692657 ,total= 1.69475913048
#vlen= 80 Time: compile= 0.236012935638 ,compute= 1.15793514252 ,total= 1.39394807816
#vlen= 80 Time: compile= 0.165726900101 ,compute= 1.16027617455 ,total= 1.32600307465
#vlen= 80 Time: compile= 0.165502071381 ,compute= 1.17049908638 ,total= 1.33600115776
#vlen= 100 Time: compile= 0.195648908615 ,compute= 0.988173007965 ,total= 1.18382191658
#vlen= 128 Time: compile= 0.24280500412 ,compute= 0.830281257629 ,total= 1.07308626175
#vlen= 256 Time: compile= 0.454282045364 ,compute= 0.458273649216 ,total= 0.91255569458
#vlen= 512 Time: compile= 0.99605512619 ,compute= 0.340112686157 ,total= 1.33616781235
#vlen= 1024 Time: compile= 2.66436100006 ,compute= 0.29629445076 ,total= 2.96065545082