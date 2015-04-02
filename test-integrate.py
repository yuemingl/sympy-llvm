from sympy import *
from sympy.abc import *

i = integrate(exp(x**2), (x,y,z))
print i
fi=lambdify([y,z],i)
print fi(1,2)
