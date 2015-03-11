import time
from jit_compile import JIT
from sympy import *
from sympy.abc import x
from ctypes import *
import matplotlib.pyplot as plt
from my_statistics import mean, std
import numpy as np

print __file__

NExpr = 10

f_exprs = []
for i in range(1,NExpr):
	expr = reduce(lambda a, b:a+b, [x**(1.0/(j+1)) for j in range(0,i)])
	f_exprs.append(expr)
	#print expr

NN=102400 #Total number of data (# of evaluation)
VectorLens = [1, 2, 4, 8, 16, 32, 64, 128]
TotalCompileTimes = []
TotalEvalTimes = []
for nData in VectorLens:
	CompileTimes = []
	EvalTimes = []
	for nTry in range(8):
		ts = time.time()
		g1 = map(lambda a:JIT().compile3([x], nData, [a]), f_exprs)
		te = time.time()
		time_compile = (te-ts)

		#Prepare parameters for call the JITed function
		outAry = (c_double*nData)()
		pX = (c_double*nData)()
		for i in range(len(pX)):
			pX[i] = 0.1

		N=NN/nData
		time_compute = 0
		for i in range(len(g1)):
			ts = time.time()
			for j in range(N):
				g1[i](byref(pX), byref(outAry))
			te = time.time()
			time_compute += (te-ts)

		CompileTimes.append(time_compile)
		EvalTimes.append(time_compute)
		print "nTry=", nTry, ",nData=", nData, ",Time: compile=", time_compile, ",compute=", time_compute, ",total=", (time_compile+time_compute)
	TotalCompileTimes.append(CompileTimes);
	TotalEvalTimes.append(EvalTimes);

print TotalCompileTimes
print TotalEvalTimes
meanCompile = map(lambda t: mean(t), TotalCompileTimes)
stdCompile  = map(lambda t: std(t), TotalCompileTimes)
meanEval    = map(lambda t: mean(t), TotalEvalTimes)
stdEval     = map(lambda t: std(t), TotalEvalTimes)
print meanCompile 
print stdCompile  
print meanEval    
print stdEval     

## Plotting ##

# Create an empty figure.
fig = plt.figure()

# Add a single axes to the figure.
ax = fig.add_subplot(1, 1, 1)

# Plot the states versus time.
width = 0.35       # the width of the bars: can also be len(x) sequence
ind = ind = np.arange(len(VectorLens))
p1 = plt.bar(ind, meanCompile,   width, color='r', yerr=stdCompile)
p2 = plt.bar(ind, meanEval, width, color='y',
             bottom=meanCompile, yerr=stdEval)

# Add a title, axes labels and a legend.
ax.set_title('Vectorized Evaluation for Ploy with Fractional Powers')
ax.set_xlabel('Vector Length')
ax.set_ylabel('Time (s)')
plt.xticks(ind+width/2., tuple(map(lambda l:str(l), VectorLens)) )
ax.legend(['JIT Compile Time', 'Evaluation Time'])

# Display the figure.
plt.show()