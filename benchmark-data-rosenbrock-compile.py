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

# (Need*1000)
#Rosenbrock lambdify(matrix) 
#N|Grad Compile Time|Grad Eval Time|Hess Compile Time|Hess Eval Time|Grad CheckSum|Hess CheckSum
lambdify = [
[5  , 0.137263059616, 0.0919940471649, 0.0186078548431, 0.0565900802612],
[55 , 0.431102991104, 0.653797149658 , 0.308935880661 , 0.598087072372 ],
[105, 0.654165029526, 1.43851399422  , 0.888613939285 , 1.47306489944  ],
[155, 0.70402097702 , 1.46867513657  , 1.42413187027  , 1.5329580307   ],
[205, 1.11419296265 , 1.81097006798  , 1.94313788414  , 2.33068799973  ],
[255, 1.21863412857 , 2.27776694298  , 2.94755220413  , 2.94281101227  ],
[305, 1.93022179604 , 2.65718913078  , 4.10849809647  , 3.57789802551  ],
[355, 1.92739295959 , 3.14450788498  , 5.25075101852  , 4.64605116844  ],
[405, 2.22623491287 , 3.9528529644   , 7.44158792496  , 5.63200187683  ],
[455, 2.2211689949  , 4.06015491486  , 9.36174416542  , 6.29428792     ],
[505, 2.62345194817 , 4.82637095451  , 11.0677549839  , 6.96997189522  ],
[555, 2.72747206688 , 5.18159294128  , 13.459913969   , 7.91085386276  ],
[605, 3.22294092178 , 5.922727108    , 16.4141049385  , 9.07861804962  ],
[655, 1.76675581932 , 3.30534505844  , 10.2653419971  , 5.57263708115  ],
[705, 1.92488098145 , 3.46923089027  , 11.6668310165  , 6.09018516541  ],
[755, 2.10820388794 , 3.73816204071  , 14.0178399086  , 7.36339616776  ],
[805, 2.15881586075 , 4.1932489872   , 15.5676839352  , 8.03694796562  ],
]
for i in range(len(lambdify)):
	row = lambdify[i]
	for j in range(1, len(row)):
		lambdify[i][j] *= 1000



#Sage fast_float onebyone v2 (Need*100)
#N|GradCompileTime|GradEvalTime|HessCompileTime|HessEvalTime|GradCheckSum|HessCheckSum
Sage = [
[5  , 0.00352311134338, 0.00253200531006, 0.00219893455505, 0.00694704055786],
[55 , 0.0483481884003 , 0.0485470294952 , 0.0536921024323 , 0.156613111496  ],
[105, 0.121881008148  , 0.126046180725  , 0.145601034164  , 0.386604070663  ],
[155, 0.202225923538  , 0.228092908859  , 0.314965963364  , 0.70232796669   ],
[205, 0.296454191208  , 0.354403972626  , 0.521248102188  , 1.09165096283   ],
[255, 0.455717086792  , 0.503686904907  , 0.807593107224  , 1.57262301445   ],
[305, 0.642210006714  , 0.708143949509  , 1.23380613327   , 2.29331707954   ],
[355, 0.803671836853  , 0.95654797554   , 1.79694008827   , 3.15543913841   ],
[405, 1.05131006241   , 1.21217298508   , 2.50188612938   , 4.03029990196   ],
[455, 1.41676998138   , 1.49681687355   , 3.50291419029   , 4.89612984657   ],
[505, 1.94949889183   , 1.94216489792   , 4.85154294968   , 6.25013399124   ],
[555, 2.45484018326   , 2.24157881737   , 6.21187806129   , 7.03913593292   ],
[605, 3.17547798157   , 2.6303358078    , 8.15538597107   , 8.16795897484   ],
[655, 3.74288511276   , 3.0974419117    , 10.1578772068   , 9.631513834     ],
[705, 4.64187788963   , 3.58673381805   , 12.4521238804   , 11.0141968727   ],
[755, 5.68853902817   , 4.05583286285   , 15.2991228104   , 12.5613880157   ],
[805, 6.58001494408   , 4.59799408913   , 18.3412630558   , 14.2840409279   ],
]
for i in range(len(Sage)):
	row = Sage[i]
	for j in range(1, len(row)):
		Sage[i][j] *= 100


aSymJava = np.array(SymJava)
aCPP = np.array(CPP)
aCPPO3 = np.array(CPPO3)
alambdify = np.array(lambdify)
aSage = np.array(Sage)

x = aSymJava[...,0]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

width = 0.25       # the width of the bars: can also be len(x) sequence
ind = np.arange(len(x))

meanCompile = aSymJava[...,1]+aSymJava[...,3]
meanEval = aSymJava[...,2]+aSymJava[...,4]
#meanCompile = map(lambda x: log(x), meanCompile)
#meanEval = map(lambda x: log(x), meanEval)
p1 = plt.bar(ind, meanCompile,   width, color='r')
p2 = plt.bar(ind, meanEval, width, color='b',
             bottom=meanCompile)

meanCompile = aCPP[...,1]
meanEval = aCPP[...,2]+aCPP[...,3]
#meanCompile = map(lambda x: log(x), meanCompile)
#meanEval = map(lambda x: log(x), meanEval)
p3 = plt.bar(ind+width, meanCompile,   width, color='r')
p4 = plt.bar(ind+width, meanEval, width, color='y',
             bottom=meanCompile)

meanCompile = aCPPO3[...,1]
meanEval = aCPPO3[...,2]+aCPPO3[...,3]
#meanCompile = map(lambda x: log(x), meanCompile)
#meanEval = map(lambda x: log(x), meanEval)
p5 = plt.bar(ind+2*width, meanCompile,   width, color='r')
p6 = plt.bar(ind+2*width, meanEval, width, color='g',
             bottom=meanCompile)


# meanCompile = aSage[...,1]
# meanEval = aSage[...,2]+aSage[...,3]
# meanCompile = map(lambda x: log(x), meanCompile)
# meanEval = map(lambda x: log(x), meanEval)
# p7 = plt.bar(ind+3*width, meanCompile,   width, color='r')
# p8 = plt.bar(ind+3*width, meanEval, width, color='m',
#              bottom=meanCompile)

# meanCompile = alambdify[...,1]
# meanEval = alambdify[...,2]+alambdify[...,3]
# meanCompile = map(lambda x: log(x), meanCompile)
# meanEval = map(lambda x: log(x), meanEval)
# p9 = plt.bar(ind+4*width, meanCompile,   width, color='r')
# p10 = plt.bar(ind+4*width, meanEval, width, color='c',
#              bottom=meanCompile)


# Add a title, axes labels and a legend.
ax.set_title('Compilation Time + Evaluation Time of the Gradient and Hessian of Rosenbrock Function')
ax.set_xlabel('Dimension of Free Variables')
ax.set_ylabel('Evaluation Time (s)')
plt.xticks(ind+width/2., tuple(map(lambda l:str(int(round(l))), x)) )
#ax.legend([p1,p2,p4,p6,p8,p10], ['Compile Time','SymJava Evaluation Time','C++  Evaluation Time','C++ O3  Evaluation Time','Sage Evaluation Time','Lambdify Evaluation Time'], loc=2)
ax.legend([p1,p2,p4,p6], ['Compile Time','SymJava Evaluation Time','C++  Evaluation Time','C++ O3  Evaluation Time'], loc=2)

# Display the figure.
plt.show()