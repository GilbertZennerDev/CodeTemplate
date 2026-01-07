from cContent import *
from pyContent import *

def runPython(imports, condition, functions, classes):
	return [pyImport(imp) for imp in imports + pyDefInports()] + [f"def {function}(): pass" for function in functions] + pyMain(condition)

def runC(imports, condition, functions):
	return [cImport(imp) for imp in imports + cDefInports()] + [f"int {function}" + "(){}" for function in functions] + cMain(condition)

