# This is a simple python dictionary program that takes any word from a user input and outputs the definition.
# Author : Kuna

import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data_definitions.json"))


def definition(word):
    word = word.lower()
    if word in data:
        print("Definition: " + "\n")
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s? Enter Y if yes or N if no : " % get_close_matches(word, data.keys())[0]).upper()
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "SORRY! The word does not exist. Please try another word."
        else:
            return "Sorry, we didn't quite understand you. Please try again."
    else:
        return "SORRY! The word does not exist. Please try another word."


word = input("Please enter the word you want to look up: ")
output = definition(word)
if type(output) == list:
    for i in output:
        print(i + "\n")
else:
    print(output)

