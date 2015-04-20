import numpy as np
import matplotlib.pyplot as plt
from math import log

#SymJava
SymJava = [
[5	, 0.025, 0.012,	0.002,	0.013],
[55	, 0.012, 0.098,	0.017,	0.071],
[105, 0.015, 0.166,	0.018,	0.127],
[155, 0.012, 0.23,	0.023,	0.2  ],
[205, 0.013, 0.307,	0.043,	0.278],
[255, 0.01,  0.389,	0.023,	0.397],
[305, 0.011, 0.453,	0.026,	0.43 ],
[355, 0.011, 0.551,	0.032,	0.52 ],
[405, 0.011, 0.604,	0.04,	0.565],
[455, 0.027, 0.691,	0.047,	0.666],
[505, 0.032, 0.799,	0.046,	0.735],
[555, 0.015, 0.827,	0.048,	0.828],
[605, 0.015, 0.905,	0.054,	0.881],
[655, 0.017, 0.978,	0.077,	1.027],
[705, 0.017, 1.096,	0.061,	1.049],
[755, 0.017, 1.128,	0.07,	1.166],
[805, 0.018, 1.197,	0.069,	1.227],
]


#g++
#     Compile    Grad       Hess
CPP = [
[5   , 0.133 , 0.012285  , 0.005769 ],
[55  , 0.176 , 0.112945  , 0.074709 ],
[105 , 0.223 , 0.205119  , 0.141377 ],
[155 , 0.289 , 0.31637   , 0.210464 ],
[205 , 0.366 , 0.417701  , 0.285483 ],
[255 , 0.381 , 0.51677   , 0.51337 ],
[305 , 0.444 , 0.617711  , 0.427058 ],
[355 , 0.484 , 0.72675   , 0.501997 ],
[405 , 0.55  , 0.820054  , 0.56362 ],
[455 , 0.603 , 0.927727  , 0.630426 ],
[505 , 0.693 , 1.02883   , 0.734305 ],
[555 , 0.734 , 1.16798   , 0.786767 ],
[605 , 0.804 , 1.26002   , 0.908035 ],
[655 , 0.854 , 1.33347   , 0.942273 ],
[705 , 0.918 , 1.4371    , 1.02455 ],
[755 , 0.974 , 1.54837   , 1.08883 ],
[805 , 1.03  , 1.66913   , 1.22527 ],
]

#g++ -O3
#     Compile    Grad       Hess
CPPO3 = [
[5   , 0.162  , 0.00555   , 0.003054 ],  
[55  , 0.32   , 0.015792  , 0.012052 ], 
[105 , 0.389  , 0.031341  , 0.025145 ], 
[155 , 0.563  , 0.048394  , 0.038475 ], 
[205 , 0.754  , 0.062533  , 0.054497 ], 
[255 , 0.964  , 0.078452  , 0.136445 ], 
[305 , 1.235  , 0.096971  , 0.083958 ], 
[355 , 1.526  , 0.110973  , 0.094553 ], 
[405 , 1.8    , 0.127781  , 0.138077 ], 
[455 , 2.135  , 0.142258  , 0.125689 ], 
[505 , 2.469  , 0.159458  , 0.199716 ], 
[555 , 2.856  , 0.176937  , 0.186688 ], 
[605 , 3.222  , 0.193468  , 0.238989 ], 
[655 , 3.403  , 0.205962  , 0.229768 ], 
[705 , 3.848  , 0.226367  , 0.305967 ], 
[755 , 4.221  , 0.23855   , 0.280694 ], 
[805 , 4.547  , 0.262885  , 0.319046 ], 
]

aSymJava = np.array(SymJava)
aCPP = np.array(CPP)
aCPPO3 = np.array(CPPO3)

x = aSymJava[...,0]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

width = 0.25       # the width of the bars: can also be len(x) sequence
ind = np.arange(len(x))

meanCompile = aSymJava[...,1]+aSymJava[...,3]
meanEval = aSymJava[...,2]+aSymJava[...,4]

p1 = plt.bar(ind, meanCompile,   width, color='r')
p2 = plt.bar(ind, meanEval, width, color='b',
             bottom=meanCompile)

meanCompile = aCPP[...,1]
meanEval = aCPP[...,2]+aCPP[...,3]

p3 = plt.bar(ind+width, meanCompile,   width, color='r')
p4 = plt.bar(ind+width, meanEval, width, color='y',
             bottom=meanCompile)

meanCompile = aCPPO3[...,1]
meanEval = aCPPO3[...,2]+aCPPO3[...,3]

p5 = plt.bar(ind+width+width, meanCompile,   width, color='r')
p6 = plt.bar(ind+width+width, meanEval, width, color='g',
             bottom=meanCompile)

# Add a title, axes labels and a legend.
ax.set_title('Compilation Time + Evaluation Time for the Gradient and Hessian of Rosenbrock Function')
ax.set_xlabel('Dimension of Free Variables')
ax.set_ylabel('Evaluation Time (s)')
plt.xticks(ind+width/2., tuple(map(lambda l:str(int(round(l))), x)) )
ax.legend([p1,p2,p4,p6], ['Compile Time','SymJava Evaluation Time','C++  Evaluation Time','C++ O3  Evaluation Time'], loc=2)

#ax.legend(['Compile Time', 'Evaluation Time', 'Evaluation Time', 'Evaluation Time'])

# Display the figure.
plt.show()