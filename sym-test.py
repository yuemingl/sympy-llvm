#!/usr/bin/env python

import time

# Import the llvmpy modules.
from llvm import *
from llvm.core import *
from llvm.ee import *                     # new import: ee = Execution Engine
import ctypes

from sympy import *
from sympy.abc import *

#expr = 2.0 * x**5 + 3.0 * x * y
expr = 2.0*x**5 + 3.0*x**4 + 5.0*x**3 + 4.5*x**2 + 5.6*x + x*y + 2.0*y**5 + 3.0*y**4 + 5.0*y**3 + 4.5*y**2 + 5.6*y + x*y
print expr
print expr.args
print expr.subs({x:2.0, y:3.0})

print "post order:"
for term in postorder_traversal(expr):
	print term.__class__, term


# Create an (empty) module.
my_module = Module.new('my_module')

ty_double = Type.double()
fun_args = []
fun_args_map = {}

for term in postorder_traversal(expr):
	if term.is_Symbol:
		idx = len(fun_args_map)
		if not term in fun_args_map: 
			fun_args_map[term] = idx

for arg in fun_args_map:
	fun_args.append(ty_double)

#	fun_args_map[term] = len(fun_args)-1
print fun_args
print fun_args_map

ty_func = Type.function(ty_double, fun_args)
fun = my_module.add_function(ty_func, "fun")
#fun.args[0].name = "a"
#fun.args[1].name = "b"

bb = fun.append_basic_block("block1")
builder = Builder.new(bb)

stack = []
for term in postorder_traversal(expr):
	if term.is_Symbol:
		stack.append(fun.args[fun_args_map[term]])
	elif term.is_Number:
		stack.append(Constant.real(ty_double, term.evalf()))
	elif term.is_Mul:
		for i in range(len(term.args)-1):
			right = stack.pop()
			left = stack.pop()
			stack.append(builder.fmul(left, right))
	elif term.is_Add:
		for i in range(len(term.args)-1):
			right = stack.pop()
			left = stack.pop()
			stack.append(builder.fadd(left, right))
	elif term.is_Pow:
		right = stack.pop()
		left = stack.pop()
		f_pow = llvm.core.Function.intrinsic(my_module, INTR_POW, [ty_double])
		stack.append(builder.call(f_pow, [left, right]))
	else:
		print "Error!"

builder.ret(stack.pop())

print my_module


# Create an execution engine object. This will create a JIT compiler
# on platforms that support it, or an interpreter otherwise.
ee = ExecutionEngine.new(my_module)

# The arguments needs to be passed as "GenericValue" objects.
arg1 = GenericValue.real(ty_double, 2.0)
arg2 = GenericValue.real(ty_double, 3.0)

# Now let's compile and run!
retval = ee.run_function(fun, [arg1, arg2])

# The return value is also GenericValue. Let's print it.
print "returned", retval.as_real(ty_double)


ct_argtypes = [ctypes.c_double, ctypes.c_double]
func_ptr_int = ee.get_pointer_to_function( fun )
FUNC_TYPE = ctypes.CFUNCTYPE(ctypes.c_double, *ct_argtypes)
py_fun = FUNC_TYPE(func_ptr_int)

print py_fun(2.0, 3.0)


N = 1000000


lfun = lambdify((x,y), expr)

ts = time.time()
for i in range(N):
	lfun(2.0, 3.0)
te = time.time()
print (te-ts)


ts = time.time()
for i in range(N):
	py_fun(2.0, 3.0)
	#ee.run_function(fun, [arg1, arg2])
te = time.time()
print (te-ts)

# ts = time.time()
# for i in range(N):
# 	expr.subs({x:2.0, y:3.0})
# te = time.time()
# print (te-ts)
