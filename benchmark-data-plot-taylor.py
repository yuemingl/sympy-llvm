import numpy as np
import matplotlib.pyplot as plt
from math import log

#-----------------------------------------Taylor Series------------------------------------------------------
#benchmark-llvm-sqrt-vectorize
#Without changing param time
llvm_vec=[
0.0375139713287,  #expr= 1.00000000000000
0.0428831577301,  #expr= 1.0*x + 1.0
0.043869972229 ,  #expr= 0.5*x**2 + 1.0*x + 1.0
0.0469710826874,  #expr= 0.166666666666667*x**3 + 0.5*x**2 + 1.0*x + 1.0
0.0498571395874,  #expr= 0.0416666666666667*x**4 + 0.166666666666667*x**3 + 0.5*x**2 + 1.0*x + 1.0
0.0539810657501,  #expr= 0.00833333333333333*x**5 + 0.0416666666666667*x**4 + 0.166666666666667*x**3 + 0.5*x**2 + 1.0*x + 1.0
0.057247877121 ,  #expr= 0.00138888888888889*x**6 + 0.00833333333333333*x**5 + 0.0416666666666667*x**4 + 0.166666666666667*x**3 + 0.5*x**2 + 1.0*x + 1.0
0.0644071102142,  #expr= 0.000198412698412698*x**7 + 0.00138888888888889*x**6 + 0.00833333333333333*x**5 + 0.0416666666666667*x**4 + 0.166666666666667*x**3 + 0.5*x**2 + 1.0*x + 1.0
0.0666389465332,  #expr= 2.48015873015873e-5*x**8 + 0.000198412698412698*x**7 + 0.00138888888888889*x**6 + 0.00833333333333333*x**5 + 0.0416666666666667*x**4 + 0.166666666666667*x**3 + 0.5*x**2 + 1.0*x + 1.0
0.068629026413 ,  #expr= 2.75573192239859e-6*x**9 + 2.48015873015873e-5*x**8 + 0.000198412698412698*x**7 + 0.00138888888888889*x**6 + 0.00833333333333333*x**5 + 0.0416666666666667*x**4 + 0.166666666666667*x**3 + 0.5*x**2 + 1.0*x + 1.0
]

#benchmark-llvm-taylor
#Without changing param time
llvm=[
3.69724583626,  #expr= 1.00000000000000
3.53579807281,  #expr= 1.0*x + 1.0
3.6428809166 ,  #expr= 0.5*x**2 + 1.0*x + 1.0
3.56534910202,  #expr= 0.166666666666667*x**3 + 0.5*x**2 + 1.0*x + 1.0
3.612210989  ,  #expr= 0.0416666666666667*x**4 + 0.166666666666667*x**3 + 0.5*x**2 + 1.0*x + 1.0
3.69063901901,  #expr= 0.00833333333333333*x**5 + 0.0416666666666667*x**4 + 0.166666666666667*x**3 + 0.5*x**2 + 1.0*x + 1.0
3.59968900681,  #expr= 0.00138888888888889*x**6 + 0.00833333333333333*x**5 + 0.0416666666666667*x**4 + 0.166666666666667*x**3 + 0.5*x**2 + 1.0*x + 1.0
3.71784496307,  #expr= 0.000198412698412698*x**7 + 0.00138888888888889*x**6 + 0.00833333333333333*x**5 + 0.0416666666666667*x**4 + 0.166666666666667*x**3 + 0.5*x**2 + 1.0*x + 1.0
3.67060804367,  #expr= 2.48015873015873e-5*x**8 + 0.000198412698412698*x**7 + 0.00138888888888889*x**6 + 0.00833333333333333*x**5 + 0.0416666666666667*x**4 + 0.166666666666667*x**3 + 0.5*x**2 + 1.0*x + 1.0
3.6263628006 ,  #expr= 2.75573192239859e-6*x**9 + 2.48015873015873e-5*x**8 + 0.000198412698412698*x**7 + 0.00138888888888889*x**6 + 0.00833333333333333*x**5 + 0.0416666666666667*x**4 + 0.166666666666667*x**3 + 0.5*x**2 + 1.0*x + 1.0
]

#sage fast_float
sage=[
1.883466959  ,   #expr= 1
1.93007493019,   #expr= x + 1
2.15443897247,   #expr= 1/2*x^2 + x + 1
2.10834407806,   #expr= 1/6*x^3 + 1/2*x^2 + x + 1
2.29894113541,   #expr= 1/24*x^4 + 1/6*x^3 + 1/2*x^2 + x + 1
2.3378880024 ,   #expr= 1/120*x^5 + 1/24*x^4 + 1/6*x^3 + 1/2*x^2 + x + 1
2.52155303955,   #expr= 1/720*x^6 + 1/120*x^5 + 1/24*x^4 + 1/6*x^3 + 1/2*x^2 + x + 1
2.62911391258,   #expr= 1/5040*x^7 + 1/720*x^6 + 1/120*x^5 + 1/24*x^4 + 1/6*x^3 + 1/2*x^2 + x + 1
2.62940788269,   #expr= 1/40320*x^8 + 1/5040*x^7 + 1/720*x^6 + 1/120*x^5 + 1/24*x^4 + 1/6*x^3 + 1/2*x^2 + x + 1
2.94319415092,   #expr= 1/362880*x^9 + 1/40320*x^8 + 1/5040*x^7 + 1/720*x^6 + 1/120*x^5 + 1/24*x^4 + 1/6*x^3 + 1/2*x^2 + x + 1
]

ufuncify=[
7.87824702263,  #expr= 1.00000000000000
7.72406387329,  #expr= 1.0*x + 1.0
7.63258385658,  #expr= 0.5*x**2 + 1.0*x + 1.0
8.61796522141,  #expr= 0.166666666666667*x**3 + 0.5*x**2 + 1.0*x + 1.0
9.39026093483,  #expr= 0.0416666666666667*x**4 + 0.166666666666667*x**3 + 0.5*x**2 + 1.0*x + 1.0
9.74567198753,  #expr= 0.00833333333333333*x**5 + 0.0416666666666667*x**4 + 0.166666666666667*x**3 + 0.5*x**2 + 1.0*x + 1.0
10.3302628994,  #expr= 0.00138888888888889*x**6 + 0.00833333333333333*x**5 + 0.0416666666666667*x**4 + 0.166666666666667*x**3 + 0.5*x**2 + 1.0*x + 1.0
10.8064610958,  #expr= 0.000198412698412698*x**7 + 0.00138888888888889*x**6 + 0.00833333333333333*x**5 + 0.0416666666666667*x**4 + 0.166666666666667*x**3 + 0.5*x**2 + 1.0*x + 1.0
11.2962200642,  #expr= 2.48015873015873e-5*x**8 + 0.000198412698412698*x**7 + 0.00138888888888889*x**6 + 0.00833333333333333*x**5 + 0.0416666666666667*x**4 + 0.166666666666667*x**3 + 0.5*x**2 + 1.0*x + 1.0
11.8332219124,  #expr= 2.75573192239859e-6*x**9 + 2.48015873015873e-5*x**8 + 0.000198412698412698*x**7 + 0.00138888888888889*x**6 + 0.00833333333333333*x**5 + 0.0416666666666667*x**4 + 0.166666666666667*x**3 + 0.5*x**2 + 1.0*x + 1.0
]

lambdify=[
1.26596498489,  #expr= 1.00000000000000
1.73784303665,  #expr= 1.0*x + 1.0
2.65794587135,  #expr= 0.5*x**2 + 1.0*x + 1.0
4.03604197502,  #expr= 0.166666666666667*x**3 + 0.5*x**2 + 1.0*x + 1.0
5.65659880638,  #expr= 0.0416666666666667*x**4 + 0.166666666666667*x**3 + 0.5*x**2 + 1.0*x + 1.0
6.98048496246,  #expr= 0.00833333333333333*x**5 + 0.0416666666666667*x**4 + 0.166666666666667*x**3 + 0.5*x**2 + 1.0*x + 1.0
8.34857487679,  #expr= 0.00138888888888889*x**6 + 0.00833333333333333*x**5 + 0.0416666666666667*x**4 + 0.166666666666667*x**3 + 0.5*x**2 + 1.0*x + 1.0
9.84851193428,  #expr= 0.000198412698412698*x**7 + 0.00138888888888889*x**6 + 0.00833333333333333*x**5 + 0.0416666666666667*x**4 + 0.166666666666667*x**3 + 0.5*x**2 + 1.0*x + 1.0
11.0206389427,  #expr= 2.48015873015873e-5*x**8 + 0.000198412698412698*x**7 + 0.00138888888888889*x**6 + 0.00833333333333333*x**5 + 0.0416666666666667*x**4 + 0.166666666666667*x**3 + 0.5*x**2 + 1.0*x + 1.0
12.3896789551,  #expr= 2.75573192239859e-6*x**9 + 2.48015873015873e-5*x**8 + 0.000198412698412698*x**7 + 0.00138888888888889*x**6 + 0.00833333333333333*x**5 + 0.0416666666666667*x**4 + 0.166666666666667*x**3 + 0.5*x**2 + 1.0*x + 1.0
]

#vec len = 10000
theano_vec=[
0.883370876312,
0.957633972168,
0.95906496048 ,
0.962067842484,
0.968122959137,
0.969844102859,
0.970263004303,
0.969112157822,
0.965795993805,
0.96966791153 ,
]

#theano function time:
theano=[
7.94146800041,
7.76174211502,
7.87686896324,
7.88205194473,
7.81489801407,
7.8935008049 ,
7.97258591652,
7.9341750145 ,
8.14559698105,
8.10303092003,
]

SymJava=[
# java.lang.Math.pow()
# 0.007,
# 0.014,
# 0.781,
# 1.451,
# 2.151,
# 2.863,
# 3.537,
# 4.287,
# 4.98 ,

#symjava.symbolic.utils.BytecodeSupport.powi()
# 0.007,
# 0.014,
# 0.166,
# 0.091,
# 0.151,
# 0.1  ,
# 0.122,
# 0.215,
# 0.174,

#batch compile
0.038, #expr=1.0
0.039, #expr=1.0 + x
0.044, #expr=1.0 + x + 0.5*pow(x,2)
0.03 , #expr=1.0 + x + 0.5*pow(x,2) + 0.16666666666666666*pow(x,3)
0.056, #expr=1.0 + x + 0.5*pow(x,2) + 0.16666666666666666*pow(x,3) + 0.041666666666666664*pow(x,4)
0.059, #expr=1.0 + x + 0.5*pow(x,2) + 0.16666666666666666*pow(x,3) + 0.041666666666666664*pow(x,4) + 0.008333333333333333*pow(x,5)
0.089, #expr=1.0 + x + 0.5*pow(x,2) + 0.16666666666666666*pow(x,3) + 0.041666666666666664*pow(x,4) + 0.008333333333333333*pow(x,5) + 0.001388888888888889*pow(x,6)
0.117, #expr=1.0 + x + 0.5*pow(x,2) + 0.16666666666666666*pow(x,3) + 0.041666666666666664*pow(x,4) + 0.008333333333333333*pow(x,5) + 0.001388888888888889*pow(x,6) + 1.984126984126984E-4*pow(x,7)
0.138, #expr=1.0 + x + 0.5*pow(x,2) + 0.16666666666666666*pow(x,3) + 0.041666666666666664*pow(x,4) + 0.008333333333333333*pow(x,5) + 0.001388888888888889*pow(x,6) + 1.984126984126984E-4*pow(x,7) + 2.48015873015873E-5*pow(x,8)
0.154, #expr=1.0 + x + 0.5*pow(x,2) + 0.16666666666666666*pow(x,3) + 0.041666666666666664*pow(x,4) + 0.008333333333333333*pow(x,5) + 0.001388888888888889*pow(x,6) + 1.984126984126984E-4*pow(x,7) + 2.48015873015873E-5*pow(x,8) + 2.7557319223985893E-6*pow(x,9)

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

CPPO3=[
0.008551,
0.011798,
0.014918,
0.015975,
0.021215,
0.026906,
0.037405,
0.047195,
0.0478,
0.052825,
]

matlab = [
1.295480,
1.941784,
1.975390,
2.020248,
2.068941,
2.113129,
2.181538,
2.244286,
2.278013,
2.35, #???
]
matlab = map(lambda x: 0.7*100*x, matlab)

mathematica = [
0.156,
0.172,
0.343,
0.484,
0.655,
0.749,
0.936,
1.108,
1.248,
1.373,
]
mathematica = map(lambda x: 0.7*100*x, mathematica)

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

# _llvm_vec   =[]
# _llvm       =[] 
# _sage       =[] 
# _ufuncify   =[] 
# _lambdify   =[] 
# _theano_vec =[] 
# _theano     =[] 
# _SymJava    =[] 
# _SymLLVM    =[] 
# _CPPO3      =[] 
# _matlab     =[] 
# _mathematica=[] 
# # for i in range(len(lambdify)): l1 .append(log(lambdify[i]/llvm_vec[i]))
# # for i in range(len(lambdify)): l2 .append(log(lambdify[i]/llvm[i]))
# # for i in range(len(lambdify)): l3 .append(log(lambdify[i]/sage[i]))
# # for i in range(len(lambdify)): l4 .append(log(lambdify[i]/ufuncify[i]))
# # for i in range(len(lambdify)): l5 .append(log(lambdify[i]/lambdify[i]))
# # for i in range(len(lambdify)): l6 .append(log(lambdify[i]/theano_vec[i]))
# # for i in range(len(lambdify)): l7 .append(log(lambdify[i]/theano[i]))
# # for i in range(len(lambdify)): l8 .append(log(lambdify[i]/SymJava[i]))
# # for i in range(len(lambdify)): l9 .append(log(lambdify[i]/SymLLVM[i]))
# # for i in range(len(lambdify)): l10.append(log(lambdify[i]/CPPO3[i]))
# # for i in range(len(lambdify)): l11.append(log(lambdify[i]/matlab[i]))
# # for i in range(len(lambdify)): l12.append(log(lambdify[i]/mathematica[i]))
# for i in range(len(lambdify)): _llvm_vec   .append(log(llvm_vec   [i]))
# for i in range(len(lambdify)): _llvm       .append(log(llvm       [i]))
# for i in range(len(lambdify)): _sage       .append(log(sage       [i]))
# for i in range(len(lambdify)): _ufuncify   .append(log(ufuncify   [i]))
# for i in range(len(lambdify)): _lambdify   .append(log(lambdify   [i]))
# for i in range(len(lambdify)): _theano_vec .append(log(theano_vec [i]))
# for i in range(len(lambdify)): _theano     .append(log(theano     [i]))
# for i in range(len(lambdify)): _SymJava    .append(log(SymJava    [i]))
# for i in range(len(lambdify)): _SymLLVM    .append(log(SymLLVM    [i]))
# for i in range(len(lambdify)): _CPPO3      .append(log(CPPO3      [i]))
# for i in range(len(lambdify)): _matlab     .append(log(matlab     [i]))
# for i in range(len(lambdify)): _mathematica.append(log(mathematica[i]))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

x = np.arange(len(llvm))

line, = plt.plot(x, SymJava    ,'s-', linewidth=1)
line, = plt.plot(x, SymLLVM    ,'D-', linewidth=1)
line, = plt.plot(x, CPPO3      ,'^--', linewidth=1)
line, = plt.plot(x, llvm_vec   ,'s-', linewidth=1)
#line, = plt.plot(x, llvm       ,'d-', linewidth=1)
line, = plt.plot(x, sage       ,'d-', linewidth=1)
line, = plt.plot(x, ufuncify   ,'h-', linewidth=1)
line, = plt.plot(x, lambdify   ,'o-',  linewidth=1)
line, = plt.plot(x, theano_vec ,'*-', linewidth=1)
line, = plt.plot(x, theano     ,'p-', linewidth=1)
line, = plt.plot(x, matlab     ,'>-', linewidth=1)
line, = plt.plot(x, mathematica,'<-', linewidth=1)

ax.set_yscale('log')
#filled_markers = (u'o', u'v', u'^', u'<', u'>', u'8', u's', u'p', u'*', u'h', u'H', u'D', u'd')
#ax.legend(['py_llvm_vec', 'py_llvm_scalar', 'sage', 'py_ufuncify', 'lambdify', 'theano_vec', 'theano_scalar', 'SymJava', 'SymLLVM', 'CPPO3','Matlab','Mathematica'],loc=4)
#ax.legend(['SymJava', 'C++_O3','Sage', 'SymPy_ufuncify', 'SymPy_lambdify', 'Theano_vector', 'Theano_scalar', 'Matlab','Mathematica'],loc=8)
#ax.set_title('Benchmark: Evaluaton for Tayor Series of e^x expanded at x=0')
ax.set_xlabel('Sum[(1/n!)x^n] for n =0,...,9')
#ax.set_ylabel('Log of Time (s)')
ax.set_ylabel('Evaluation Time (second)')
#ax.set_ylabel('Speed up (log)')


plt.annotate('SMC_Java',       xy=(x[-1]-2,      SymJava[-1]    +0))
plt.annotate('C++_O3',         xy=(x[-1]-2,      CPPO3[-1]      -0.03))
plt.annotate('Sage',           xy=(x[-1]-2,      sage[-1]       -0))
plt.annotate('SymPy_ufuncify', xy=(x[-1]-5,      ufuncify[-1])       )
plt.annotate('SymPy_lambdify', xy=(x[1],         lambdify[3]    -0))
plt.annotate('Theano_vector',  xy=(x[-1]-2.5,      theano_vec[-1] -0))
plt.annotate('Theano_scalar',  xy=(x[-1]-2.5,      theano[-1]     -3))
plt.annotate('Matlab',         xy=(x[-1]-2,      matlab[-1]     -0))
plt.annotate('Mathematica',    xy=(x[-1]-3,      mathematica[-1]-0))
plt.annotate('SMC_C++',        xy=(x[-1]-3,      SymLLVM[-1]-0))
plt.annotate('SMC_Py',         xy=(x[-1]-2,      llvm_vec[-1]+0.01))



plt.show()