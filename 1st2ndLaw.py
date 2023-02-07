from Modules.ConceptList import *

# Import the modules required
import json
from difflib import get_close_matches
from openpyxl import *
  
# Loading data from json file
# in python dictionary
#data = json.load(open("dictionary.json"))

wb = Workbook("ConceptsSheet.xlsx")







data = {}


  
# Driver code
word = input("Enter word: ")
output = translate(word)
  
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
input('Press ENTER to exit') 