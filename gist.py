import urllib2
import json
import os
from Tkinter import Tk

# Print title
print "GIST.py  by Matt \'TheFrostlixen\' Fredrickson 2015"

# Get username to query from and make the JSON API request
username = raw_input("Username: ")
http = urllib2.urlopen('https://api.github.com/users/{0}/gists'.format(username))
jsData = json.loads( http.read().decode("utf-8") )
print "--------"

# Get all of the user's gists, display as description & files
for index in range( len(jsData) ):
	# Find all of the files for the gist
	files = ""
	for key,el in jsData[index]["files"].items():
		if files != "":
			files += ", " # comma separation!
		files += key

	# Display gist with files listed below
	print "{0}.\t{1}".format(index, jsData[index]["description"])
	print "\t[{0}]".format(files)
	print ""

# Get gist id from user selection 
selection = raw_input("Select Gist index: ")
id = jsData[int(selection)]["id"]
print "\'{0}\' copied to clipboard.".format(id)

# copy ID to user's clipboard (ungodly hack, this is mildly gross but works xplatform so hey)
hwnd = Tk()
hwnd.withdraw()
hwnd.clipboard_clear()
hwnd.clipboard_append( id )

# wait for user input to kill
raw_input()
hwnd.destroy()
