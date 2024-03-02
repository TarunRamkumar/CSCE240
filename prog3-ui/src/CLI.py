import FileParser as Parser
import string
import re
#Creates a class to handle the UI
class CLI:
    def __init__(self):
        #To run in global terminal 
        self.google = Parser.FileParser("..\\data\\Google10k-4Q-2024.txt")
        self.generalMotors = Parser.FileParser("..\\data\\GeneralMotors10k-4Q-2024.txt")
        
        #To run in VSCode terminal
        # self.google = Parser.FileParser("prog3-ui\data\Google10k-4Q-2024.txt")
        # self.generalMotors = Parser.FileParser("prog3-ui\data\GeneralMotors10k-4Q-2024.txt")
        
    #Method to process the user's response
    def processResponse(self,response):
        #Lowers the response to prevent case sensitivity
        response = response.lower()
        #Searches for GM, if not found then defaults to Google
        if re.search('(^|\s)gm',response) != None or  re.search("general motors",response) != None:
            part = re.findall('part \d',response)
            #if all is searched, returns the entire file
            if "all" in response or "everything" in response:
                return self.generalMotors.getFile()
            #If part is found, writes the numbers to roman numerals and then searches for the part
            elif len(part) > 0:
                for item in part:
                    item = self.writeRoman(item)
                    print(item+ " shown below: ")
                    return self.generalMotors.searchParts(item)
            #Prints the table of contents
            elif re.search('(^|\s)toc(\s|$)',response) != None or re.search('table of contents',response) != None:
                return self.generalMotors.tableOfContents
            #Finds the item and returns it
            else:
                for item in self.generalMotors.listTOC:
                    splitItem = str(item).split('. ')
                    for part in splitItem:
                        if re.search(part.lower()+'$',response):
                            return self.generalMotors.searchItems(item)
                return "Error with input. Cannot find: " + response + " in file. Please make sure it is included within the TOC"
        #Same thing as above, but for Google
        else:
            part = re.findall('part \d',response)
            if "all" in response or "everything" in response:
                return self.google.getFile()
            elif len(part) > 0:
                for item in part:
                    item = self.writeRoman(item)
                    print(item+ " shown below: ")
                    return self.google.searchParts(item)
            elif re.search('(^|\s)toc(\s|$)',response) != None or re.search('table of contents',response) != None:
                return self.google.tableOfContents
            else:
                for item in self.google.listTOC:
                    splitItem = str(item).split('. ')
                    for part in splitItem:
                        if re.search(part.lower()+'$',response):
                            return self.google.searchItems(item)
                return "Error with input. Cannot find: " + response + " in file. Please make sure it is included within the TOC"
            
    #Converts the part query to roman numerals, in case the user prefers to input numerals
    def writeRoman(self,word):
        newWord = ""
        romanDict = { 
            1:"I",
            2:"II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI"
            }
        for char in word:
            if char.isdigit():
                newWord += romanDict[int(char)]
            else:
                newWord += char
        return newWord
        #return ''.join([romanDict[int(char)] if char.isdigit() else char for char in word])

        
ui = CLI()
run = True
while run:
    #Runs until the user quits
    response = input("What would you like to ask about? Type q or quit to exit")
    if response == "q" or response == "quit":
        print("Have a nice day!")
        run = False
    else:
        print(ui.processResponse(response))
   
    