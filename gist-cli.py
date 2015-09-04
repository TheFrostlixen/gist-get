# Header title
print "GIST-CLI.py  by Matt \'TheFrostlixen\' Fredrickson 2015\n--------"

# Links input text to relevant function/operation
def interpret_cmd(arg):
	switch = {
		'a': toString('hello'),
		'b': toString( 0 ),
	}
	return switch.get( arg, "Command \'{0}\' not recognized...\nAvailable commands: {1}".format(arg,printHelp(switch.items())) )
	
# Gist function definitions
def toString(arg):
	return str(arg)

def printHelp(arr):
	help = ""
	for key,val in arr:
		if help != "":
			help += ", " # comma separation!
		help += key
	return help

# Program loop
while True:
	cmds = raw_input('$ ').split()
	if len(cmds) > 0:
		print interpret_cmd( cmds[0] )
