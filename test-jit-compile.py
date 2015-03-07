from jit_compile import JIT
from sympy.abc import x
from ctypes import *

func = JIT().compile([x], x+x)
print "Scala return value function:",func(1)


exprs = [x, x**2, x**3]
func = JIT().compile2([x], exprs)

print "Vector return values by parameter reference"
#Need a buffer
outAry = (c_double*len(exprs))()
print "Before call:"
for i in outAry: print i,
N=100000
for i in range(N):
	func(2.0,byref(outAry))
print "\nAfter call:"
for i in outAry: print i,
