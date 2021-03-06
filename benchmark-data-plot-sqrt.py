import numpy as np
import matplotlib.pyplot as plt
from math import log

#-----------------------------------------Ploy with Fractional Powers-------------------------------------------------------
llvm_vec = [
#vlen=128
0.0682580471039,
0.677155971527 ,
1.25157594681  ,
1.84160709381  ,
2.41642284393  ,
2.98730587959  ,
3.56346201897  ,
4.14961910248  ,
4.74849295616  ,
# #vlen=256
# 0.037257194519,
# 0.640280008316,
# 1.21580410004 ,
# 1.80925416946 ,
# 2.38864803314 ,
# 3.00670194626 ,
# 3.61068415642 ,
# 4.2643969059  ,
# 4.89458703995 ,
]

llvm = [
3.50151109695,
4.04695487022,
4.58365797997,
5.21860003471,
5.76458215714,
6.20199203491,
6.77218604088,
7.4955060482 ,
8.06003522873,
]


sage = [
5.96055078506,
6.05862402916,
5.93401217461,
6.09424686432,
6.09410905838,
5.9449198246 ,
6.04044818878,
6.06557106972,
5.94781494141,
]

ufuncify = [
7.96253705025,
7.87664294243,
8.78509807587,
9.33145308495,
9.97222709656,
10.3883759975,
10.766947031 ,
11.2898588181,
11.4600138664,
]

lambdify = [
1.86726713181,
3.04771709442,
4.0152220726 ,
5.23916387558,
6.23207306862,
7.33628582954,
8.46323394775,
9.58110308647,
10.5341880322,
]

theano_vec = [
0.869971036911,
0.987299919128,
1.39320397377 ,
1.91916298866 ,
2.42727303505 ,
2.93831396103 ,
3.44927096367 ,
4.08599281311 ,
5.02067494392 ,
]

theano=[
74.1050848961,
71.7205440998,
72.3560888767,
73.5202741623,
74.6754498482,
75.8028309345,
77.20499897  ,
77.0179371834,
77.8787260056,
]

SymJava=[
0.009,
0.046,
1.466,
2.109,
2.847,
3.531,
4.196,
4.927,
5.616,
]


SymLLVM=[
0.00883,
0.539747,
1.04788,
1.57559,
2.0867,
2.59586,
3.11325,
3.63486,
4.14237,
]

CPPO3=[
0.011553,
0.542694,
1.0587,
1.60821,
2.12228,
2.64062,
3.15616,
3.68752,
4.20648,
]

#R2012b
matlab = [
2.082214,
1.993762,
2.079215,
2.111780,
2.071818,
2.051798,
2.051378,
2.077770,
2.072889,
]
matlab = map(lambda x: 0.7*100*x, matlab)

mathematica = [
0.172,
0.328,
0.468,
0.608,
0.78,
0.92,
1.045,
1.201,
1.341,
]
mathematica = map(lambda x: 0.7*100*x, mathematica)

# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# x = np.arange(len(llvm))+1
# line, = plt.plot(x, llvm_vec,   's-', linewidth=1)
# line, = plt.plot(x, llvm,       'd-', linewidth=1)
# line, = plt.plot(x, sage,       'o-', linewidth=1)
# line, = plt.plot(x, ufuncify,   '>-', linewidth=1)
# line, = plt.plot(x, lambdify,   '<-', linewidth=1)
# line, = plt.plot(x, theano_vec, '*-', linewidth=1)
# ax.legend(['llvm_vec', 'llvm_scalar', 'sage', 'ufuncify', 'lambdify', 'theano_vec'])
# ax.set_title('Benchmark: 10M Evaluaton for Ploy with Fractional Powers')
# ax.set_xlabel('Sum[x^(1/n)] for n =1,...,9')
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
x = np.arange(len(llvm))+1
# x = np.arange(len(llvm)-1)+2
# l1.pop(0)
# l2.pop(0)
# l3.pop(0)
# l4.pop(0)
# l5.pop(0)
# l6.pop(0)
# l7.pop(0)
# l8.pop(0)
# l9.pop(0)

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


# #line, = plt.plot(x, l1, 's-', linewidth=1)
# #line, = plt.plot(x, l2, 'd-', linewidth=1)
# line, = plt.plot(x, l3, 'o-', linewidth=1)
# line, = plt.plot(x, l4, '>-', linewidth=1)
# line, = plt.plot(x, l5, '-', linewidth=1)
# line, = plt.plot(x, l6, '*-', linewidth=1)
# line, = plt.plot(x, l7, 'p-', linewidth=1)
# line, = plt.plot(x, l8, 'h-', linewidth=1)
# #line, = plt.plot(x, l9, 'D-', linewidth=1)
# line, = plt.plot(x, l10, '<-', linewidth=1)
# line, = plt.plot(x, l11, 's-', linewidth=1)
# line, = plt.plot(x, l12, 'd-', linewidth=1)

ax.set_yscale('log')
#filled_markers = (u'o', u'v', u'^', u'<', u'>', u'8', u's', u'p', u'*', u'h', u'H', u'D', u'd')
#ax.legend(['py_llvm_vec', 'py_llvm_scalar', 'sage', 'py_ufuncify', 'lambdify', 'theano_vec', 'theano_scalar', 'SymJava', 'SymLLVM', 'CPPO3','Matlab','Mathematica'],loc=4)
#ax.legend(['SymJava', 'C++_O3','Sage', 'SymPy_ufuncify', 'SymPy_lambdify', 'Theano_vector', 'Theano_scalar', 'Matlab','Mathematica'],loc=8)
#ax.set_title('Benchmark: Evaluaton for Ploynormial with Fractional Powers')
ax.set_xlabel('Sum[x^(1/n)] for n =1,...,9')
#ax.set_xlabel('Sum[x^(1/n)] for n =2,...,9')
#ax.set_ylabel('Log of Time (s)')
ax.set_ylabel('Evaluation Time (second)')
#ax.set_ylabel('Speed up (log)')


plt.annotate('SMC_Java',        xy=(x[1]+0.2,      SymJava[1]    +0))
plt.annotate('C++_O3',         xy=(x[1]-0.5,      CPPO3[1]      -0.36))
plt.annotate('Sage',           xy=(x[2]+0.3,      sage[1]       +0.5))
plt.annotate('SymPy_ufuncify', xy=(x[3]-0,      ufuncify[3]   +2)       )
plt.annotate('SymPy_lambdify', xy=(x[0]+0.1,         lambdify[1]    +0.5))
plt.annotate('Theano_vector',  xy=(x[0]+0.3,      theano_vec[1] +0.3))
plt.annotate('Theano_scalar',  xy=(x[1]-0,      theano[1]+10     -0))
plt.annotate('Matlab',         xy=(x[1]-0,      matlab[1]+10     -0))
plt.annotate('Mathematica',    xy=(x[0]+0.2,      mathematica[2]-0))
plt.annotate('SMC_C++',        xy=(x[1]-0.5,      SymLLVM[1]-0.45))
plt.annotate('SMC_Py',  xy=(x[0]+0.1,      llvm_vec[1]-0.3))


plt.show()

