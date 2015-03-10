from jit_compile import JIT
from sympy.abc import x, y
from ctypes import *

vlen = 3
exprs = [x+y**0.5, 2*x-y]
func = JIT().compile3([x, y], vlen, exprs)

print "Vector return values by parameter reference"
#Need a buffer
outLen = vlen*len(exprs)
outAry = (c_double*outLen)(1,2,3)
print "Before call:"
for i in outAry: print i,

pX = (c_double*vlen)(*[1.0,2.0,3.0])
pY = (c_double*vlen)(*[30.0,20.0,10.0])

func(byref(pX), byref(pY), byref(outAry))
print "\nAfter call:"
for i in outAry: print i,
