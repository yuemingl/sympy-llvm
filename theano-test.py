#from theano import *
import time
import theano.tensor as T
#from theano import function
from theano import *
from theano.compile import *
from theano.compile.function import *
from sympy.printing.theanocode import theano_function

x = T.dscalar('x')
y = T.dscalar('y')
expr = x + y

#theano.compile.function_dump("a", [x, y], expr)
f = function([x, y], expr)
print f(2,3)

fn_theano = theano_function([x,y], [expr], dims={x: 1, y:1}, dtypes={x: 'float64'})
print fn_theano(2,3)

xx = T.dvector('xx')
yy = T.dvector('yy')
expr_vec = xx + yy
vec_dim = 1
fn_theano_vec = theano_function([xx,yy], [expr_vec]) #, dims={xx: vec_dim, yy: vec_dim}, dtypes={x: 'float64'})
print fn_theano_vec([2,2],[3,3])



NN = 100000

ts = time.time()
for i in range(NN):
	f(2,3)
te = time.time()
print "theano function: ",(te-ts)

ts = time.time()
for i in range(NN):
	fn_theano(2,3)
te = time.time()
print "sympy.printing.theanocode.theano_function: ",(te-ts)

nData = 100
N=NN/nData
ts = time.time()
aryX = [2.0 for i in range(nData)]
aryY = [3.0 for i in range(nData)]
for i in range(N):
	r = fn_theano_vec(aryX, aryY)
te = time.time()
print r
print "theano function (vectorized): ",(te-ts)
