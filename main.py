# -*- coding: utf-8 -*-
from PyDictionary import PyDictionary
import requests
import json

def getLongestSyn(word):
    api_url = "http://pydictionary-geekpradd.rhcloud.com/api/synonym/"
    longest = ""

    response = requests.get(api_url + word)

    if(response.ok):
        syns = json.loads(response.content)
        for syn in syns:
            if len(syn) > len(longest):
                longest = syn
            print longest + ", " + syn
    else:
        print "Bad things happened"
    return longest

usedWords = []
filedata = None
dictionary = PyDictionary()
minWordLength = 5

newString = ""
with open('data.txt', 'r') as file:
  filedata = file.read()

for word in filedata.split():
    if len(word) >= minWordLength:
        newString += str(getLongestSyn(word))
    else:
        newString += str(word)
    newString += " "
    
print newString
