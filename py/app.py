#python app.py app.py -f func1 -c class1
#ech fuegen nach den if ac < 2 etc zou
#-condition bla: if ac bla: exit()

import sys
from helpers import *
from getters import *
from cContent import *
from pyContent import *
from mainFunctions import *

def main():
	av, ac, ftype = getAvAc()
	print(f"filetype {ftype}")
	checks(ac, av)
	imports = getImports(ac, av)
	condition = getCondition(ac, av)
	functions = getFunctions(ac, av)
	classes = getClasses(ac, av)
	if ftype == "py": saveFile(av, runPython(imports, condition, functions, classes), ftype)
	if ftype == "c": saveFile(av, runC(imports, condition, functions), ftype)
if __name__ == '__main__': main()
