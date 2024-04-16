import FileParser as Parser
import string
import re
from difflib import SequenceMatcher as matcher
from datetime import datetime
import csv
import os

#Creates a class to handle the UI
class CLI:
    def __init__(self):
        #To run in global terminal 
        # try:
        #     self.google = Parser.FileParser("..\\data\\Google10k-4Q-2024.txt")
        #     self.generalMotors = Parser.FileParser("..\\data\\GeneralMotors10k-4Q-2024.txt")
        # except:
        #     print("File not found. Please ensure that the correct files have been loaded into the data folder and try again.")
        #To run in VSCode terminal
        self.google = Parser.FileParser("prog3-ui\data\Google10k-4Q-2024.txt")
        self.generalMotors = Parser.FileParser("prog3-ui\data\GeneralMotors10k-4Q-2024.txt")
    
    #Cleans the response to better match the queries
    def cleanResponse(self,response):
        response = re.sub( "((^|\s)gm)|(general motors)","",response)
        utterance = list(response.strip().lower().split(" "))
        stopwords = []
        #common stopwords in the english language
        with open("..\\data\\stopwords.txt") as file:
            for line in file:
                stopwords.append(line.strip())
        
        i = 0
        #Removes stopwords from the user's input
        while i < len(utterance):
            if utterance[i] in stopwords:
                utterance.remove(utterance[i])
            else:
                i+=1
        
        # i = 0
        # if "part" in utterance:
        #     for word in utterance:
        #         utterance[i] = self.writeRoman(word)
        #         i+=1
        return utterance
    
    #Calculates a percentage match between the query and user input
    def match(self,response, query):
        utterance = response
        matchPercent = 0
        commonWords = 0
        for word1 in utterance:
            for word2 in query:
                #Checks the percentage match between words
                if matcher(a=word1,b=word2).ratio() > 0.75:
                    commonWords +=1
        #commonWords = utterance.intersection(query)
        totalWords = set(utterance).union(set(query))
        matchPercent = commonWords/len(totalWords)
        return matchPercent
    
    #Changes roman numerals to numbers
    def writeRoman(self,word):
        newWord = word
        romanDict = { 
            "I":1,
            "II":2,
            "III":3,
            "IV":4,
            "V":5,
            "VI":6
            }
        if word.upper() in romanDict:
            newWord = str(romanDict.get(word.upper()))
    
        return newWord
    #Processes the query for matching, by removing special characters, roman numerals, and stopwords
    def cleanQuery(self,query):
        query = self.writeRoman(query)
        query = re.sub("\.","",query)
        return self.cleanResponse(query)
    
    #Matches teh responses and returns the closest match
    def matchResponses(self,response,company):
        matchPercent = 0
        match = None
        supportedQueries = company.listTOC
        response = self.cleanResponse(response)
        for query in supportedQueries:
            cleanedQuery = self.cleanQuery(query)
            score = self.match(response,cleanedQuery)
            if score > matchPercent:
                matchPercent = score
                match = query
        return str(match), str(round(matchPercent * 100,2))
            
    #Processes the user input
    def processResponse(self,response):
        #Lowers the response to prevent case sensitivity
        response = response.lower()
        #Searches for GM, if not found then defaults to Google
        if re.search('(^|\s)gm',response) != None or  re.search(" general motors",response) != None:
            if "all" in response or "everything" in response:
                    return str(self.generalMotors.getFile())
            elif re.search('(^|\s)toc(\s|$)',response) != None or re.search('table of contents',response) != None:
                return str(self.generalMotors.tableOfContents)
            else:
                match = self.matchResponses(response,self.generalMotors)
                confirmation = input("I am "+match[1]+" confident you are searching for " + match[0]+" in GM. Is this correct? Type 'y' or 'yes' to continue, anything else to exit and try again.")
                if confirmation.lower() == "y" or confirmation.lower() == "yes":
                    return str(self.generalMotors.processedFile.get(match[0]))
                else:
                    return "User exited, please enter a new search to try again."
        #Same thing as above, but for Google
        else:
            if "all" in response or "everything" in response:
                    return str(self.google.getFile())
            elif re.search('(^|\s)toc(\s|$)',response) != None or re.search('table of contents',response) != None:
                return str(self.google.tableOfContents)
            else:
                match = self.matchResponses(response,self.google)
                confirmation = input("I am "+match[1]+" confident you are searching for " + match[0]+" in Google. Is this correct? Type 'y' or 'yes' to continue, anything else to exit and try again.")
                if confirmation.lower() == "y" or confirmation.lower() == "yes":
                    return str(self.google.processedFile.get(match[0]))
                else:
                    return "User exited, please enter a new search to try again."
            
            
            
    #Converts the part query to roman numerals, in case the user prefers to input numerals
    
        #return ''.join([romanDict[int(char)] if char.isdigit() else char for char in word])
        
        

        
ui = CLI()
run = True
chatSessions = os.listdir("..\\data\\chat_sessions")
chatSessionCount = len(chatSessions)
filename = os.path.join('..','data', 'chat_sessions','session-'+str(chatSessionCount+1)+'_'+str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))+'.txt')  
starttime = datetime.now()
userUtterances = 0
systemUtterances = 0
with open(filename,"w",encoding="utf-8") as file:   
    while run:
        #Runs until the user quits
            response = input("What would you like to ask about? Type q or quit to exit")
            userUtterances+=1
            file.write("User input: "+response+'\n')
            if response == "q" or response == "quit":
                systemUtterances+=1
                print("Have a nice day!")
                file.write("System Response: Have a nice day!\n")
                with open("..//data//chat_statistics.csv","a",encoding="utf-8") as logFile:
                    totaltime = datetime.now()-starttime
                    log = csv.writer(logFile)
                    log.writerow([datetime.now().strftime("%Y-%m-%d"),starttime.strftime("%H:%M:%S"),str(totaltime.total_seconds()),userUtterances,systemUtterances])
                run = False
            else:
                systemResponse = ui.processResponse(response)
                systemUtterances+=1
                print(systemResponse)
                file.write("System Response: " + systemResponse+'\n')
   
    