# -*- coding: utf-8 -*-
import requests
import json
import logging

LOG_FILENAME = 'TheSaurus.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

def TheSaurus():
    usedWords = []
    inFile = None
    outFile = None
    minWordLength = 5

    newString = ""
    with open('data.txt', 'r') as file:
      inFile = file.read()

    for word in inFile.split():
        if len(word) >= minWordLength:
            newSyn = str(getLongestSyn(word, usedWords))
            if newSyn != "":            #If getLongestSyn finds a new synonym, append to new string. Otherwise, append the original word
                newString += newSyn
                usedWords.append(newSyn)
            else:
                newString += word
        else:
            newString += str(word)
        newString += " "

    with open('example_output.txt', 'w') as outFile:
        outFile.write(newString)

def getLongestSyn(word, usedWords):
    api_url = "http://pydictionary-geekpradd.rhcloud.com/api/synonym/"
    longest = ""

    response = requests.get(api_url + word)     #Query API for synonyms

    if(response.ok):
        syns = json.loads(response.content)
        logging.debug(word + ": " + str(syns))

        for syn in syns:
            if len(syn) > len(longest):
                if syn not in usedWords:
                    longest = syn
            print longest + ", " + syn
    else:
        print "Bad things happened"

    return longest

if __name__ == "__main__":
    TheSaurus()
