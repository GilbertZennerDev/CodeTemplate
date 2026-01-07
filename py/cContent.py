def cDefInports():
	return ["unistd.h", "stdio.h", "stdlib.h", "fcntl.h", "string.h", "sys/wait.h", "string", "iostream"]

def cImport(name):
	return f"#include <{name}>"

def cMain(condition):
	if condition == []: line = "\tif (0)"
	else: line = f"\t\tif (ac {condition[0]})" 
	return [
	"\nint\tmain(int ac, char **av)",
	"{",
	line,
	"\t\treturn (1);",
	"\treturn (0);",
	"}" 
	]
