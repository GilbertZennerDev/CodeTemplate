def saveFile(av, lines, ftype):
	for line in lines: print(line)
	open(f"app.{ftype}", "w").write("\n".join(lines))

def checks(ac, av):
	if ac < 2: exit()
#	if av[1] == "app.py": print("Name cannot be app.py"); exit()
#	for i in range(1, ac - 1, 2):
		#if av[i][0] != '-' and av[i][1] not in 'fci': exit()
#		if av[i] != '-f' and av[i] != '-c' and av[i] != '-i' and av[i] != '-condition': exit()
