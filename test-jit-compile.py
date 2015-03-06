from jit_compile import JIT
from sympy.abc import x


func = JIT().compile([x], x+x)
print func(1)