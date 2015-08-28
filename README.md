#Gist-Get API

A very simple Python CLI script that uses GitHub's API to allow users to quickly retrieve Gists hosted here on GitHub.

The Idea
-
The idea behind this project is to create a lightweight, portable interface to GitHub's Gists. Since gists are somewhat difficult to use on-the-fly, I wanted something to serve as a front-end interface to enable a much easier and cleaner experience with Gists.

How It Works
-
It simply uses a JSON string from GitHub's publicly available API, and parses that information to get the description, files, and ID for each of the user's Gists. Upon selection, it will copy the ID to the user's clipboard, for use for cloning/pulling/pushing as the user decides.

In The Future
-
It'd be nice to flesh this out a little bit more, into a comprehensive package for managing Gists (i.e. able to clone to a specified location, push/pull, etc.). I'll get around to it once I have a bit more free time and ability to work on this.

>Note: I did not encapsulate this in a class as a design decision. I decided that for the sake of convenience, it would be better as a simple script for now.
