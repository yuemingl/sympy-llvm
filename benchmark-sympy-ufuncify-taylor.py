import time

import ctypes
from sympy import *
from sympy.abc import x

from sympy.utilities.autowrap import ufuncify
from sympy.utilities.lambdify import lambdify

print __file__

NExpr = 10

f_exprs = []
for i in range(1,NExpr):
	expr = reduce(lambda a, b:a+b, [1.0/factorial(j)*x**j for j in range(0,i)])
	f_exprs.append(expr)
	print expr

ts = time.time()
g1 = map(lambda a:ufuncify([x], a), f_exprs)
te = time.time()
print g1
print "sympy ufuncify compile time: ",(te-ts)
print "sympy ufuncify eval value= "
for g in g1:
	print g(0.1)

ts = time.time()
#g2 = map(lambda a:lambdify([x], a, modules='math'), f_exprs) #11.0926191807
#g2 = map(lambda a:lambdify([x], a, modules='mpmath'), f_exprs) #11.0835108757
g2 = map(lambda a:lambdify([x], a, modules='numpy'), f_exprs) #10.9833340645
#g2 = map(lambda a:lambdify([x], a, modules='numexpr'), f_exprs) #73.1567411423 
#g2 = map(lambda a:lambdify([x], a, modules='sympy'), f_exprs) #11.0603320599
te = time.time()
print g2
print "sympy lambdify compile time: ",(te-ts)
print "sympy lambdify eval value= "
for g in g2:
	print g(0.1)

N=10000000
for i in range(len(f_exprs)):
	ts = time.time()
	for j in range(N):
		g1[i](0.1)
	te = time.time()
	print "sympy ufuncify time: ", (te-ts), " expr=", f_exprs[i] 

for i in range(len(f_exprs)):
	ts = time.time()
	for j in range(N):
		g2[i](0.1)
	te = time.time()
	print "sympy lambdify time: ", (te-ts), " expr=", f_exprs[i] 