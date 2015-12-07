#Gist-Get API

##gist.py

A very simple Python CLI script that uses GitHub's API to allow users to quickly retrieve Gists hosted on GitHub.

The Idea
-
The idea behind this project is to create a lightweight, portable interface to GitHub's Gists. Since gists are somewhat difficult to use on-the-fly, I wanted something to serve as a front-end interface to enable a much easier and cleaner experience with Gists.

How It Works
-
It simply uses a JSON string from GitHub's publicly available API, and parses that information to get the description, files, and ID for each of the user's Gists. Upon selection, it will copy the ID to the user's clipboard, for use for cloning/pulling/pushing as the user decides.

>Note: I did not encapsulate this in a class as a design decision. I decided that for the sake of convenience, it would be better as a simple script for now.

##gist-cli.py & simulator.py

This project now contains a Gist command line interpretter (gist-cli.py), and a terminal simulator for running commands through said interpretter (simulator.py).

Usage
-
You may either:

- Execute *simulator.py* and run gist commands through that **OR**

- Execute *gist-cli.py {arg1} {arg2} ...* in your terminal.

>Note: On Unix systems (or Windows systems without Python in the PATH), you must prepend the "python" command in your terminal. You'll need to change gist-cli.py to start after the 2nd argument, otherwise you'll end up with the file path in your arg list.

