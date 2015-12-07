import urllib2
import json
from Tkinter import Tk

# Header title
print "GIST.py  by Matt \'TheFrostlixen\' Fredrickson 2015"

# Get username to query and make the JSON API request
username = raw_input("Username: ")
http = urllib2.urlopen('https://api.github.com/users/{0}/gists'.format(username))
jsData = json.loads( http.read().decode("utf-8") )

# Set up for clipboard ops
hwnd = Tk()
hwnd.withdraw()

while True:
	# Print header/username info
	print "--------\nDisplaying GISTs for user {0}".format(username)

	# Menu option 0 for Quit.
	print "0.\tQuit\n"

	# Get all of the user's gists, display as description + files
	for index in range( len(jsData) ):
		# Find all of the files for the gist
		files = ""
		for key,el in jsData[index]["files"].items():
			if files != "":
				files += ", " # comma separation!
			files += key

		# Display gist with files listed below
		print "{0}.\t{1}\n\t[{2}]\n".format(index+1, jsData[index]["description"], files)

	# Retrieve gist id based on user input (0 to quit)
	selection = int( raw_input("Select Gist index: ") )
	if selection == 0:
		break
	id = jsData[selection-1]["git_pull_url"]

	# copy ID to user's clipboard
	hwnd.clipboard_clear()
	hwnd.clipboard_append( id )
	print "\'{0}\' copied to clipboard.".format(id)

# Destroy window for clipboard ops
hwnd.destroy()

