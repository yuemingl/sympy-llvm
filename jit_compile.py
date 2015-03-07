# Import the llvmpy modules.
import ctypes
#import random
import math
import uuid

from llvm import *
from llvm.core import *
from llvm.ee import *                     # new import: ee = Execution Engine

from sympy import *

def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class JIT:
	# Create an (empty) module.
	func_module = Module.new("func_module")

	# Create an execution engine object. This will create a JIT compiler
	# on platforms that support it, or an interpreter otherwise.
	ee = ExecutionEngine.new(func_module)

	def compile(self, args, expr):
		ty_double = Type.double()

		# #Automaticall extract arguments from expression
		# fun_args_map = {}
		# for term in postorder_traversal(expr):
		# 	if term.is_Symbol:
		# 		idx = len(fun_args_map)
		# 		if not term in fun_args_map: 
		# 			fun_args_map[term] = idx

		# fun_args = []
		# for arg in fun_args_map:
		# 	fun_args.append(ty_double)

		fun_args = [ty_double for arg in args]
		fun_args_map = {}
		for i in range(len(args)):
			fun_args_map[args[i]] = i

		#print fun_args
		#print fun_args_map

		ty_func = Type.function(ty_double, fun_args)
		#fun = self.func_module.add_function(ty_func, "fun"+str(random.random()))
		fun = self.func_module.add_function(ty_func, "fun"+str(uuid.uuid1()).replace("-",""))
		#fun.args[0].name = "a"
		#fun.args[1].name = "b"

		bb = fun.append_basic_block("block1")
		builder = Builder.new(bb)

		stack = []
		for term in postorder_traversal(expr):
			if term.is_Symbol:
				stack.append([fun.args[fun_args_map[term]], 0.0])
			elif term.is_Number:
				stack.append([Constant.real(ty_double, term.evalf()), term.evalf()])
			elif term.is_Mul:
				for i in range(len(term.args)-1):
					right = stack.pop()[0]
					left = stack.pop()[0]
					stack.append([builder.fmul(left, right), 0.0])
			elif term.is_Add:
				for i in range(len(term.args)-1):
					right = stack.pop()[0]
					left = stack.pop()[0]
					stack.append([builder.fadd(left, right), 0.0])
			elif term.is_Function:
				if term.__class__ == sin:
					param = stack.pop()[0]
					ifun = llvm.core.Function.intrinsic(self.func_module, INTR_SIN, [ty_double])
					stack.append([builder.call(ifun, [param]), 0.0])
				elif term.__class__ == cos:
					param = stack.pop()[0]
					ifun = llvm.core.Function.intrinsic(self.func_module, INTR_COS, [ty_double])
					stack.append([builder.call(ifun, [param]), 0.0])
			elif term.is_Pow:
				tmp = stack.pop()
				right = tmp[0]
				left = stack.pop()[0]
				#print isinstance(right, Constant)
				#print dir(right)
				#print right.type.kind
				if tmp[1] == math.floor(tmp[1]):
					right = right.fptosi(Type.int())
					f_pow = llvm.core.Function.intrinsic(self.func_module, INTR_POWI, [ty_double])
				else:
					f_pow = llvm.core.Function.intrinsic(self.func_module, INTR_POW, [ty_double])
				stack.append([builder.call(f_pow, [left, right]), 0.0])
			else:
				print "ERROR: Unknown function in expression!"

		builder.ret(stack.pop()[0])
		#print self.func_module

		ct_argtypes = [ctypes.c_double for arg in args]
		func_ptr_int = self.ee.get_pointer_to_function( fun )
		FUNC_TYPE = ctypes.CFUNCTYPE(ctypes.c_double, *ct_argtypes)
		py_fun = FUNC_TYPE(func_ptr_int)

		return py_fun
