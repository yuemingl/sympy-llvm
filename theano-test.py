#from theano import *
import time
import theano.tensor as T
from theano import function
from sympy.printing.theanocode import theano_function

x = T.dscalar('x')
y = T.dscalar('y')
expr = x + y

f = function([x, y], expr)
print f(2,3)

NN = 100000

ts = time.time()
for i in range(NN):
	f(2,3)
te = time.time()
print "theano function: ",(te-ts)


fn_theano = theano_function([x,y], [expr], dims={x: 1, y:1}, dtypes={x: 'float64'})
print fn_theano(2,3)

ts = time.time()
for i in range(NN):
	fn_theano(2,3)
te = time.time()
print "theano_function: ",(te-ts)

from sympy import *
from sympy.abc import *
from sympy.utilities.autowrap import ufuncify
expr = x + y
print expr
fn_fortran = ufuncify([x,y], expr)
print fn_fortran(2.0, 3.0)

ts = time.time()
for i in range(NN):
	fn_fortran(2.0, 3.0)
te = time.time()
print "ufuncify: ",(te-ts)