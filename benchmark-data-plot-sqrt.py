import numpy as np
import matplotlib.pyplot as plt

#-----------------------------------------Ploy with Fractional Powers-------------------------------------------------------
llvm_vec = [
# #vlen=128
# 0.0682580471039,
# 0.677155971527 ,
# 1.25157594681  ,
# 1.84160709381  ,
# 2.41642284393  ,
# 2.98730587959  ,
# 3.56346201897  ,
# 4.14961910248  ,
# 4.74849295616  ,
#vlen=256
0.037257194519,
0.640280008316,
1.21580410004 ,
1.80925416946 ,
2.38864803314 ,
3.00670194626 ,
3.61068415642 ,
4.2643969059  ,
4.89458703995 ,
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

l1=[]
for i in range(len(lambdify)):
	l1.append(lambdify[i]/llvm_vec[i])
l2=[]
for i in range(len(lambdify)):
	l2.append(lambdify[i]/llvm[i])
l3=[]
for i in range(len(lambdify)):
	l3.append(lambdify[i]/sage[i])
l4=[]
for i in range(len(lambdify)):
	l4.append(lambdify[i]/ufuncify[i])
l5=[]
for i in range(len(lambdify)):
	l5.append(lambdify[i]/lambdify[i])
l6=[]
for i in range(len(lambdify)):
	l6.append(lambdify[i]/theano_vec[i])
l7=[]
for i in range(len(lambdify)):
	l7.append(lambdify[i]/theano[i])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x = np.arange(len(llvm))
x = np.arange(len(llvm)-1)+2
l1.pop(0)
l2.pop(0)
l3.pop(0)
l4.pop(0)
l5.pop(0)
l6.pop(0)
l7.pop(0)

line, = plt.plot(x, l1, 's-', linewidth=1)
line, = plt.plot(x, l2, 'd-', linewidth=1)
line, = plt.plot(x, l3, 'o-', linewidth=1)
line, = plt.plot(x, l4, '>-', linewidth=1)
#line, = plt.plot(x, l5, '<-', linewidth=1)
line, = plt.plot(x, l6, '*-', linewidth=1)
line, = plt.plot(x, l7, 'p-', linewidth=1)
ax.legend(['llvm_vec', 'llvm_scalar', 'sage', 'ufuncify', 'theano_vec', 'theano_scalar'])
ax.set_title('Benchmark: 10M Evaluaton for Ploy with Fractional Powers')
ax.set_xlabel('Sum[x^(1/n)] for n =2,...,9')
ax.set_ylabel('Speed up')
plt.show()

