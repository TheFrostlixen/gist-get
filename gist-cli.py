#-------------------------#
# AUTHOR: Matt Fredrickson
# GITHUB: TheFrostlixen
# DATE: 
#-------------------------#
import sys
import json
from os import system
from urllib2 import urlopen, HTTPError

### TODO:
### 	implement clone
### 	make gist independent of git
### 	yank individual files (not clone the repo)

# Links input text to relevant function/operation
def interpret_cmd(cmd, args):
	# build a dictionary of commands to functions
	switch = {
		'list': list,
		'clone': None,
		'push': push,
		'pull': pull,
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

### argv : 0:user, 1:filename, 2+:git clone args
def clone( argv ):
	# find user repo with matching filenames
		# find any duplicates and prompt for user selection?
	# retrieve git_pull_url
	# run system 'git clone' to retrieve
	return ""

### argv : git push args
def push( argv ):
	try:
		system('git push ' + argv )
	except:
		return 'git push failed'

### argv : git pull args
def pull( argv ):
	try:
		system('git pull ' + argv )
	except:
		return 'git pull failed'
	
# === Internal helper functions ===
def GrabJson( argv ):
	# grab JSON data from github api
	try:
		http = urlopen( 'https://api.github.com/users/{0}/gists'.format(argv[0]) )
		jsData = json.loads( http.read().decode("utf-8") )
	except HTTPError, ValueError:
		raise Exception("ERROR: Could not find or parse gist data.")
	except IndexError:
		raise Exception("ERROR: Username not supplied.")
	return jsData

# === System-level entry point ===
cmds = sys.argv[1:]
if len(cmds) > 0:
	print interpret_cmd( cmds[0], cmds[1:] )
