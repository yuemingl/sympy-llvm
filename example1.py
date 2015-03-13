from jit_compile import JIT
from sympy import *
from sympy.abc import x, y
R = 0.127-(x*0.194/(y+0.194));
Rdy = R.diff(y);
print  Rdy
jit = JIT()
func = jit.Compile([x, y], Rdy)
print func(0.362, 0.556)
