#-------------------------#
# AUTHOR: Matt Fredrickson
# GITHUB: TheFrostlixen
# DATE: APR 29 2016
#-------------------------#
import sys
import json
from os import system
from urllib.request import urlopen, HTTPError

# Links input text to relevant function/operation
def interpret_cmd(cmd, args):
	# build a dictionary of commands to functions
	switch = {
		'help': help,
		'list': list,
		'clone': clone,
		'cloned': cloned,
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
	msg = ""			# start blank to avoid prepended commas
	for key,val in arr:
		if msg != "":	# add the comma separation! (only when items are already listed though)
			msg += ", "
		else:			# string is empty so start building
			msg = "Command \'{0}\' not recognized...\nAvailable commands: ".format(c)
		msg += key		# finally, add the command string itself
	return msg

# === Gist-CLI function definitions ===
def help( argv ):
	if argv and argv[0] == "help":
		print("u cheeky bugger")
	elif argv and argv[0] == "list":
		print("LIST [USERNAME]")
		print("  Program will list all gists that belong to a given user.")
		print("  Displays gist description, files associated, and repo ID.")
		print(" USERNAME: Username on GitHub.")
	elif argv and argv[0] == "clone":
		print("CLONE [USERNAME]/[FILE] [ARGS]")
		print("  Clones the repository from [USERNAME] containing [FILENAME].")
		print("  Operates using 'GIT CLONE' and supplies the appropriate repo URL.")
		print(" USERNAME: Username on GitHub.")
		print(" FILE: A file contained within a gist on GitHub.")
		print(" ARGS: Any valid arguments for a normal 'GIT CLONE' command.")
	elif argv and argv[0] == "cloned":
		print("CLONED [USERNAME]/[DESC] [ARGS]")
		print("  Clones the repository from [USERNAME] with a description containing [DESC].")
		print("  Operates using 'GIT CLONE' and supplies the appropriate repo URL.")
		print("  If DESC is more than one word, it should be contained within quotes as follows:")
		print("   cloned thefrostlixen/\"my description from a gist\"")
		print(" USERNAME: Username on GitHub.")
		print(" DESC: A string contained within a gist's description on GitHub.")
		print(" ARGS: Any valid arguments for a normal 'GIT CLONE' command.")
	else:
		print("Available commands: ")
		print("    HELP")
		print("        Show this help message, or detailed help about another command.")
		print("    LIST [USERNAME]")
		print("        List all gists that belong to the username supplied.")
		print("    CLONE [USERNAME]/[FILE] [ARGS]")
		print("        Clone the repository from [USERNAME] containing [FILENAME].")
		print("    CLONED [USERNAME]/[DESC] [ARGS]")
		print("        Clone the repository from [USERNAME] with a description containing [DESC].")
	return ""

### argv : [USERNAME]
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
		string += "{0}.\t{1} ({2})\n\t[{3}]\n\n".format(index+1, jsData[index]["description"], jsData[index]["id"], files)
	
	if len(jsData) == 0:
		return "ERROR: No gists found for user '{0}'.".format(argv[0])
	return string.strip();

### argv : 0:[USERNAME]/[FILENAME], 1+:git clone args
def clone( argv ):
	try:
		search = argv[0].split('/')
		try:
			jsData = GrabJson( search )
		except Exception as ex:
			return ex
		
		if len(jsData) == 0:
			raise IndexError('Repo path not supplied.')
		for index in range( len(jsData) ):
			for key,el in jsData[index]["files"].items():
				if key.lower() == search[1].lower():
					result = jsData[index]["git_pull_url"];
					result += " " + " ".join( argv[1:] )
					system("git clone " + result)
	except IndexError as ie:
		return "ERROR: Repo path not supplied.";
	except UnboundLocalError as ue:
		return "ERROR: Could not find or parse gist data."
		
	return ""

### argv : 0:[USERNAME]/[DESC], 1+:git clone args
def cloned( argv ):
	try:
		search = argv[0].split('/')
		try:
			jsData = GrabJson( search )
		except Exception as ex:
			return ex
		
		if len(jsData) == 0:
			raise IndexError('Repo path not supplied.')
		for index in range( len(jsData) ):
			if search[1].lower() in jsData[index]["description"].lower():
				result = jsData[index]["git_pull_url"];
				result += " " + " ".join( argv[1:] )
				system("git clone " + result)
	except IndexError:
		return "ERROR: Repo path not supplied.";
	except UnboundLocalError:
		return "ERROR: Could not find or parse gist data."
	except AttributeError:
		return "ERROR: Gist data is invalid."
		
	return ""

# === Internal helper functions ===
def GrabJson( argv ):
	# grab JSON data from github api
	try:
		http = urlopen( 'https://api.github.com/users/{0}/gists'.format(argv[0]) )
		jsData = json.loads( http.read().decode("utf-8") )
	except (HTTPError, ValueError):
		raise Exception("ERROR: Could not find or parse gist data.")
	except IndexError:
		raise Exception("ERROR: Username not supplied.")
	return jsData

# === System-level entry point ===
cmds = sys.argv[1:]
if len(cmds) > 0:
	try:
		print(interpret_cmd( cmds[0], cmds[1:] ))
		print
	except KeyboardInterrupt:
		print
