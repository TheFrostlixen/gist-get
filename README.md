#Gist-Get CLI

A very simple Python CLI script that uses GitHub's API to allow users to quickly retrieve Gists hosted on GitHub. This uses [Github's API](https://developer.github.com/v3/) which *does* have a [limit](https://developer.github.com/v3/#rate-limiting) for how many times it can be called per hour.

The Idea
-
The idea behind this project is to create a lightweight, portable interface to GitHub's Gists. Since gists are somewhat difficult to use on-the-fly (as they use non-intuitive repo names), I wanted something to serve as a front-end to enable a much easier and cleaner experience with Gists.

How It Works
-
This project utilizes a command-line interpreter to enable users to pull JSON data from GitHub's publicly available API. 

Installation/Usage
-
Using it is simple! Eventually I am going to set this up so all you need to do is run a script to install this interpreter (plus dependencies if necessary). Then to use it, you will just have to type `"gist [cmd] ..."`.

>Note: I did not encapsulate this in a class as a design decision. I decided that for the sake of convenience, it would be better as a simple script for now.

##gist-menu.py

This was my first go at creating a Gist interface. It uses a menu to display all of the gists (by description and files) a particular user has, and allows the user to select one. It outputs a string that is the repo name, and will copy the repo name to the user's clipboard.

##gist.py & simulator.py

Simulator.py is intended to be a reusable test environment for the interpreter script, without having to reload the environment each time a change is made to the script. It is just a terminal simulator that pipes commands to the actual program (gist.py).

Usage
-
You may either:

- Execute `simulator.py` and run gist commands through that **OR**

- Execute `gist.py {arg1} {arg2} ...` in your terminal.

>Note: On systems without Python available in the environment (i.e. Windows %PATH%), you must prepend the "python" command in your terminal. You'll need to change gist.py to start after the *2nd argument* instead of the 1st, otherwise you'll end up with the file path in your arg list.

