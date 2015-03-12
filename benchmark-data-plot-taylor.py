import numpy as np
import matplotlib.pyplot as plt
from math import log

#-----------------------------------------Taylor Series------------------------------------------------------
llvm_vec=[
0.039134979248 ,
0.0466578006744,
0.0468530654907,
0.0490889549255,
0.0530180931091,
0.0567910671234,
0.0594549179077,
0.0683329105377,
0.0687310695648,
]

llvm=[
3.47477483749,
3.57408905029,
3.47729301453,
3.67761206627,
3.5669631958 ,
3.46216797829,
3.57206201553,
3.57880496979,
3.53235793114,
]

sage=[
1.83930516243,
2.00562596321,
2.01100683212,
2.08117794991,
2.28247404099,
2.27572798729,
2.41463088989,
2.63132190704,
2.58098220825,
]

ufuncify=[
7.99719905853,
7.8732612133 ,
7.77631092072,
8.71262288094,
9.18606209755,
9.87490200996,
10.1178441048,
10.5825340748,
11.1187059879,
]

lambdify=[
1.31747102737,
1.68059802055,
2.87474584579,
4.20905900002,
5.715695858  ,
7.15989995003,
8.31176805496,
9.67445516586,
11.135641098 ,
]

theano_vec=[
0.889164924622,
0.976317882538,
0.974488973618,
0.974408864975,
0.975341796875,
0.990405082703,
0.983306884766,
0.978288888931,
0.980741977692,
]

theano=[
73.8917908669,
71.4365959167,
71.5178279877,
78.7809510231,
72.6675970554,
73.3062839508,
74.5479679108,
73.915309906 ,
76.4422588348,
]

SymJava=[
0.007,
0.014,
0.781,
1.451,
2.151,
2.863,
3.537,
4.287,
4.98 ,
]

SymLLVM=[
0.001794,
0.001676,
0.001672,
0.002529,
0.003131,
0.003551,
0.003629,
0.004573,
0.004784,
0.005324,
]
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# x = np.arange(len(llvm))
# line, = plt.plot(x, llvm_vec,   's-', linewidth=1)
# line, = plt.plot(x, llvm,       'd-', linewidth=1)
# line, = plt.plot(x, sage,       'o-', linewidth=1)
# line, = plt.plot(x, ufuncify,   '>-', linewidth=1)
# line, = plt.plot(x, lambdify,   '<-', linewidth=1)
# line, = plt.plot(x, theano_vec, '*-', linewidth=1)
# ax.legend(['llvm_vec', 'llvm_scalar', 'sage', 'ufuncify', 'lambdify', 'theano_vec'])
# ax.set_title('Benchmark: 10M Evaluaton for Tayor Series of e^x at x=0')
# ax.set_xlabel('Sum[(1/n!)x^n] for n =0,...,8')
# ax.set_ylabel('Time (s)')
# plt.show()

l1=[]
l2=[] 
l3=[] 
l4=[] 
l5=[] 
l6=[] 
l7=[] 
l8=[] 
l9=[] 
for i in range(len(lambdify)): l1.append(log(lambdify[i]/llvm_vec[i]))
for i in range(len(lambdify)): l2.append(log(lambdify[i]/llvm[i]))
for i in range(len(lambdify)): l3.append(log(lambdify[i]/sage[i]))
for i in range(len(lambdify)): l4.append(log(lambdify[i]/ufuncify[i]))
for i in range(len(lambdify)): l5.append(log(lambdify[i]/lambdify[i]))
for i in range(len(lambdify)): l6.append(log(lambdify[i]/theano_vec[i]))
for i in range(len(lambdify)): l7.append(log(lambdify[i]/theano[i]))
for i in range(len(lambdify)): l8.append(log(lambdify[i]/SymJava[i]))
for i in range(len(lambdify)): l9.append(log(lambdify[i]/SymLLVM[i]))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x = np.arange(len(llvm))
line, = plt.plot(x, l1, 's-', linewidth=1)
line, = plt.plot(x, l2, 'd-', linewidth=1)
line, = plt.plot(x, l3, 'o-', linewidth=1)
line, = plt.plot(x, l4, '>-', linewidth=1)
#line, = plt.plot(x, l5, '<-', linewidth=1)
line, = plt.plot(x, l6, '*-', linewidth=1)
line, = plt.plot(x, l7, 'p-', linewidth=1)
line, = plt.plot(x, l8, 'h-', linewidth=1)
line, = plt.plot(x, l9, 'D-', linewidth=1)
ax.legend(['llvm_vec', 'llvm_scalar', 'sage', 'ufuncify', 'theano_vec', 'theano_scalar', 'SymJava', 'SymLLVM'])
ax.set_title('Benchmark: 10M Evaluaton for Tayor Series of e^x at x=0')
ax.set_xlabel('Sum[(1/n!)x^n] for n =0,...,8')
ax.set_ylabel('Speed up (log)')
plt.show()