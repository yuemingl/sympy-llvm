from jit_compile import JIT
from sympy.abc import x
from ctypes import *

func = JIT().Compile([x], x+x)
print "Scala return value:",func(1)


exprs = [x, x**2, x**3]
func = JIT().BatchCompile([x], exprs)

print "Batch return values (pass by parameter)"
#Output buffer
outAry = (c_double*len(exprs))()
print "Before call:"
for i in outAry: print i,
N=100000
for i in range(N):
	func(2.0,byref(outAry))
print "\nAfter ",N," call:"
for i in outAry: print i,
