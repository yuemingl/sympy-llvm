from sympy import *
from sympy.physics.mechanics import *
from sympy.physics.mechanics import mechanics_printing
from jit_compile import JIT
from numpy import sin, cos, linspace, zeros
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from ctypes import *
import time
import sys

ts = time.time()
q1, q2 = dynamicsymbols('q1 q2')
q1d, q2d = dynamicsymbols('q1 q2', 1)
u1, u2 = dynamicsymbols('u1 u2')
u1d, u2d = dynamicsymbols('u1 u2', 1)
l, m, g = symbols('l m g')

N = ReferenceFrame('N')
A = N.orientnew('A', 'Axis', [q1, N.z])
B = N.orientnew('B', 'Axis', [q2, N.z])

A.set_ang_vel(N, u1 * N.z)
B.set_ang_vel(N, u2 * N.z)

O = Point('O')
P = O.locatenew('P', l * A.x)
R = P.locatenew('R', l * B.x)

O.set_vel(N, 0)
P.v2pt_theory(O, N, A)
R.v2pt_theory(P, N, B)

ParP = Particle('ParP', P, m)
ParR = Particle('ParR', R, m)

kd = [q1d - u1, q2d - u2]
FL = [(P, m * g * N.x), (R, m * g * N.x)]
BL = [ParP, ParR]


KM = KanesMethod(N, q_ind=[q1, q2], u_ind=[u1, u2], kd_eqs=kd)


KM.kanes_equations(FL, BL)
kdd = KM.kindiffdict()
mass_matrix = KM.mass_matrix_full
forcing_vector = KM.forcing_full
#mprint(mass_matrix)
#mprint(forcing_vector)
qudots = mass_matrix.inv() * forcing_vector
#mprint(qudots)
qudots = qudots.subs(kdd)
# mprint(qudots)
# qudots.simplify()
# mprint(qudots)

#JIT compile the symbol functions
x1, x2, x3, x4 = symbols('x1 x2 x3 x4')
dim = qudots.shape

qudots_ary = []
for i in range(dim[0]):
    qudots_ary.append(qudots[i,0].subs([(q1, x1),(q2, x2),(u1, x3),(u2, x4)]))
ary_len = len(qudots_ary)

func = JIT().BatchCompile([l,m,g,x1,x2,x3,x4], qudots_ary)

def rhs(y, t, l, m, g):
    q1 = y[0]
    q2 = y[1]
    u1 = y[2]
    u2 = y[3]
    dydt = zeros((len(y)))
    outAry = (c_double*ary_len)()
    func(l,m,g,q1,q2,u1,u2,byref(outAry))
    for i in range(len(outAry)):
        dydt[i] = outAry[i]
    #return outAry
    return dydt
symbolTime = time.time()-ts
 
ts = time.time()
# Specify the length, mass and acceleration due to gravity.
parameters = (1, 1, 9.8)
# Specify initial conditions for the states.
y0 = [.1, .2, 0, 0]
# Create a time vector.
NN = 100
if len(sys.argv) >= 2:
    NN = int(sys.argv[1])

t = linspace(0, 5, NN)
# Integrate the equations of motion.
y = odeint(rhs, y0, t, parameters)
#print y
evalTime = time.time()-ts
print NN, symbolTime, evalTime, symbolTime+evalTime


## Plotting ##

# Create an empty figure.
#fig = plt.figure()

# Add a single axes to the figure.
#ax = fig.add_subplot(1, 1, 1)

# Plot the states versus time.
#ax.plot(t, y)

# Add a title, axes labels and a legend.
#ax.set_title('Double Pendulum Example')
#ax.set_xlabel('Time (s)')
#ax.set_ylabel('Angle, Angluar rate (rad, rad/s)')
#ax.legend(['q1', 'q2', 'u1', 'u2'])

# Display the figure.
#plt.show()
