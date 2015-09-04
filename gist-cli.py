import sys

# Links input text to relevant function/operation
def interpret_cmd(arg):
	switch = {
		'a': toString('hello'),
		'b': toString( 12 ),
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

# Program 
#cmds = process.argv.split()
#if len(cmds) > 0:
#	print interpret_cmd( cmds[0] )
for s in sys.argv:
	print s