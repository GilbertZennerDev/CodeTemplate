import sys

def getStuff(ac, av, symbol):
	return [av[i] for i in range(3, ac, 2) if av[i - 1] == symbol and '-' not in av[i]]

def getImports(ac, av):
	return getStuff(ac, av, '-i')

def getCondition(ac, av):
	return getStuff(ac, av, '-condition')

def getFunctions(ac, av):
	return getStuff(ac, av, '-f')

def getClasses(ac, av):
	return getStuff(ac, av, '-c')

def getAvAc():
	return sys.argv, len(sys.argv), sys.argv[1]
