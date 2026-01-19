import sys

#=====================C++

def printBasicCpp():
	condition = input("What is the ac condition?\n")
	try:
		content = open("basic.c", 'r').read()
		content = content.replace("CONDITION", "if (ac " + condition + ") return ;")
		open("test.c", 'w').write(content)
	except Exception as e:
		print(e); return

#=====================C++

def loadFunction(newname, newargs, newbody):
	try:
		content = open("function.py", 'r').read()
		content = content.replace("FUNCNAME", newname).replace("ARGS", newargs).replace("FUNCBODY", newbody)
		return content
	except Exception as e:
		print(e); return

def printBasicPython():
	condition = input("What is the ac condition?\n")
	try:
		content = open("basic.py", 'r').read()
		content = content.replace("CONDITION", "if ac " + condition + ": return")
		open("test.py", 'w').write(content)
	except Exception as e:
		print(e); return

#=====================Main

def main():
	av = sys.argv
	ac = len(av)
	if ac != 3: print("Usage python3 app.py py basic\n"); exit();
	lang = av[1]
	arg = av[2]
	if arg == "basic":
		if lang == "py":
			printBasicPython()
		elif lang == "c++":
			printBasicCpp()

if __name__ == "__main__":main()
