from os import system

# Header title
print("GIST-CLI.py  by Matt \'TheFrostlixen\' Fredrickson 2015\n--------")

# Program loop
while True:
	cmds = input('$ ')
	if len(cmds) > 0:
		system("gist.py " + cmds)
