import numpy as np
import matplotlib.pyplot as plt

#-----------------------------------------Ploy with Fractional Powers-------------------------------------------------------
llvm_vec = [
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

]


# Create an empty figure.
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x = np.arange(len(llvm))+1
line, = plt.plot(x, llvm_vec,   's-', linewidth=1)
line, = plt.plot(x, llvm,       'd-', linewidth=1)
line, = plt.plot(x, sage,       'o-', linewidth=1)
line, = plt.plot(x, ufuncify,   '>-', linewidth=1)
line, = plt.plot(x, lambdify,   '<-', linewidth=1)
line, = plt.plot(x, theano_vec, '*-', linewidth=1)
ax.legend(['llvm_vec', 'llvm_scalar', 'sage', 'ufuncify', 'lambdify', 'theano_vec'])
ax.set_title('Benchmark: 100M Evaluaton for Ploy with Fractional Powers')
ax.set_xlabel('Sum[x^(1/n)] for n =1,...,9')
ax.set_ylabel('Time (s)')
plt.show()

