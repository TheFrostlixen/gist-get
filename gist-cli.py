import sys

# Links input text to relevant function/operation
def interpret_cmd(cmd, args):
	# build a dictionary of commands to functions
	switch = {
		'a': func1,
		'b': func2,
	}
	
	# execute function call or return help message
	func = switch.get( cmd, printHelp(cmd,switch.items()) )
	return func()

# Print command error & help message (available commands)
def printHelp(c, arr):
	help = ""			# start blank to avoid prepended commas
	for key,val in arr:
		if help != "":	# add the comma separation! (only when items are already listed though)
			help += ", "
		else:			# string is empty so start building
			help = "Command \'{0}\' not recognized...\nAvailable commands: ".format(c)
		help += key		# finally, add the command string itself
	return help

# Gist-CLI function definitions
def func1():
	print "fail"
	return 'hello'

def func2():
	return 'world'

# System-level entry point
cmds = sys.argv[1:]
if len(cmds) > 0:
	print interpret_cmd( cmds[0], cmds[1:] )
