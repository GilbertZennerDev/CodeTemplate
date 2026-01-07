nameLine= "if __name__ == '__main__': main()"

def pyDefInports():
	return ["sys"]

def pyImport(name):
	return f"import {name}"

def pyMain(condition):
	if condition == []: line = ""
	else: line = f"\tif ac {condition[0]}: return"
	return [
	"def\tmain():",
	"\tav = sys.argv",
	"\tac = len(av)",
	line,
	nameLine
	]
