import urllib2
import json
import os

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
print id

# clone the gist to local system (or some other method of copying)
os.system("git clone https://gist.github.com/{0}.git".format(id))

# wait for user input to kill
raw_input()
