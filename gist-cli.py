import sys
import json
from urllib2 import urlopen, HTTPError

# Links input text to relevant function/operation
def interpret_cmd(cmd, args):
	# build a dictionary of commands to functions
	switch = {
		'list': list,
		'clone': None,
		'push': None,
		'pull': None,
	}
	
	# retrieve function pointer
	func = switch.get( cmd )
	
	# execute function call or return help message
	try:
		value = func( args )
	except TypeError:
		value = printHelp( cmd, switch.items() )
	
	return value

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

# === Gist-CLI function definitions ===
### argv : username
def list( argv ):
	# get JSON data for supplied username
	try:
		jsData = GrabJson( argv )
	except Exception as ex:
		return ex
	
	# Get all of the user's gists, display as description + files
	string = ""
	for index in range( len(jsData) ):
		# Find all of the files for the gist
		files = ""
		for key,el in jsData[index]["files"].items():
			if files != "":
				files += ", " # comma separation!
			files += key
		
		# Display gist with files listed below
		string += "{0}.\t{1}\n\t[{2}]\n\n".format(index+1, jsData[index]["description"], files)
	
	return string;

# === Internal helper functions ===
def GrabJson( argv ):
	# grab JSON data from github api
	try:
		http = urlopen( 'https://api.github.com/users/{0}/gists'.format(argv[0]) )
		jsData = json.loads( http.read().decode("utf-8") )
	except HTTPError:
		raise Exception("ERROR: Could not find or parse gist data.")
	except IndexError:
		raise Exception("ERROR: Username not supplied.")
	return jsData

# === System-level entry point ===
cmds = sys.argv[1:]
if len(cmds) > 0:
	print interpret_cmd( cmds[0], cmds[1:] )
