import nlopt
from numpy import *
from jit_compile import JIT
import sympy as sm

x1,x2,a,b = sm.symbols('x1 x2 a b')
obj = sm.sqrt(x2)
ctr =(a*x1+b)**3 - x1

jit = JIT()
objGrad1 = jit.Compile([x1, x2], obj.diff(x1))
objGrad2 = jit.Compile([x1, x2], obj.diff(x2))
ctrGrad1 = jit.Compile([x1, x2, a, b], ctr.diff(x1))
ctrGrad2 = jit.Compile([x1, x2, a, b], ctr.diff(x2))

def myfunc(x, grad):
    if grad.size > 0:
        grad[0] = objGrad1(x[0], x[1])
        grad[1] = objGrad2(x[0], x[1])
    return sqrt(x[1])

def myconstraint(x, grad, a, b):
    if grad.size > 0:
        grad[0] = ctrGrad1(x[0], x[1], a, b)
        grad[1] = ctrGrad2(x[0], x[1], a, b)
    return (a*x[0] + b)**3 - x[1]

opt = nlopt.opt(nlopt.LD_MMA, 2)
opt.set_lower_bounds([-float('inf'), 0])
opt.set_min_objective(myfunc)
opt.add_inequality_constraint(lambda x,grad: myconstraint(x,grad,2,0), 1e-8)
opt.add_inequality_constraint(lambda x,grad: myconstraint(x,grad,-1,1), 1e-8)
opt.set_xtol_rel(1e-4)
x = opt.optimize([1.234, 5.678])
minf = opt.last_optimum_value()
print "optimum at ", x[0],x[1]
print "minimum value = ", minf
print "result code = ", opt.last_optimize_result()
