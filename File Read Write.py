# This code sample introduces two new things: 1) regex expressions and 2) python functions
# Have a look at these links for more - we can go through this tomorrow. See if you can incoporate this snippet into your version of "File Read Write"
# Python regex - https://www.w3schools.com/python/python_regex.asp
# Python functions - https://www.w3schools.com/python/python_functions.asp

# The code starts at line 19 - the "def" lines are called later on in the code but not executed before line 19

import re
import random

lines = ["This is an <<id>> line", "This is another test <<amt>> line", "And another test line"]

def generate_id():
     return str(random.randint(1000,9999))

def generate_amt():
    return str('{0:.2f}'.format(round((random.random() * 100), 2)))
     
for line in lines:
    match = re.search("<<.*>>", line)
    if match != None:
        if match.group() == "<<id>>":
            outputLine = line.replace(match.group(),generate_id())
        elif match.group() == "<<amt>>":
            outputLine = line.replace(match.group(),generate_amt())
        else:
            outputLine = line
    else:
        outputLine = line
    print(outputLine)