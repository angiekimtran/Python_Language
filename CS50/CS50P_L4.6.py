# Practice programs using APIs, pip, requests library, and JSON library
# Requests is a HTTP library that allows you to make web requests using python code
# Requests allows you to automate the retrieval of URLs that start with HTTP or HTTPS
# A package is a collection of modulesS
# A library is a collection of packages

# Creating a program that pretends to be a browser, connects to that third-party API on a server and download some data that can then be incorporated into my program
# The program below uses Apple's iTunes API so that I can get information about the songs of a particular band/artist
# In the command-line, users can specify the artist they are interested in, then the program will take data from Apple's API to generate 20 songs from the artist
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=20&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])