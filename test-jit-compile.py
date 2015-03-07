from jit_compile import JIT
from sympy.abc import x


func = JIT().compile([x], x+x)
print func(1)

func = JIT().compile2([x], x+x)
print func(1)
