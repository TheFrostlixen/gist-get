import os

# Header title
print "GIST-CLI.py  by Matt \'TheFrostlixen\' Fredrickson 2015\n--------"

# Program loop
while True:
	cmds = raw_input('$ ')
	if len(cmds) > 0:
		os.system("(gist.py " + cmds + ")")
