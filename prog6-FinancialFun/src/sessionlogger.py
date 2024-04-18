import csv #importing csv library
import os #importing os library
import re #importing re library

#Dev's PA5 code

def summary(n): #prints the summary of a single chat session
    count = 0 #creates a variable named count and sets it to 0
    with open("../data/chat_statistics.csv") as f: #opens the csv file
        csvReader = csv.reader(f) #creates a csv file reader
        i = 1
        for row in csvReader:
            #Gets the next chatNum because rows start at 2 while chatnums start at 1
            if(int(n) == i):
                return f"Chat {n} has {row[3]} user inputs and {row[4]} system responses, with a total session time of {row[2]} seconds"
            i+=1
    if (int(n)>=i): #checks to see if the value of input value is greater than or equal to the value of count
        #prints the statement below
        return "Error. There are only "+str(i)+" sessions. Please choose a valid number. The session numbers go from 0 to "+str(i-1)+"."
    f.close() #closes the file

#Combination of my PA5 and Dev's chat retrieval code
def showchat(n): #prints the entire chat to the terminal
    fileString = "" #creates a fileName variable
    count = 0 #creates a variable named count and sets it to 0
    sessionFiles = os.listdir("..\\data\\chat_sessions")
    #Logic for showchat command
        #Checks to see if valid chat value
    if int(n) <= len(sessionFiles):
        chatSession = sessionFiles[int(n)-1]
        #Special characters not parsable with utf-8, thus had to encode with cp1252
        with open(os.path.join("..\\data\\chat_sessions",chatSession),"r",encoding="cp1252") as file:
            for line in file:
                fileString += line
    if (int(n)>=len(sessionFiles)): #checks to see if the input value is greater than or equal to the value of count
        #prints the statement below
        return "Error. There are only "+str(count)+" sessions. Please choose a valid number. The session numbers go from 0 to "+str(count-1)+"."
    return "Chat "+n+" chat is:\n" + fileString

#My chat summary code from PA5
def getAllChatSummary():
    with open("..\\data\\chat_statistics.csv","r") as logFile:
        log = csv.reader(logFile)
        totalUser = 0
        totalSystem = 0
        totalTime = 0
        totalChats = 0
        for row in log:
            #Skips the headings row
            if len(row) == 0 or row is None or not row[0] == "Session Date":
                print(row)
                totalChats+=1
                totalTime += float(row[2])
                totalSystem += int(row[4])
                totalUser += int(row[3])
        return f"There are {totalChats} total chats to date, with {totalUser} total user inputs and {totalSystem} system responses. The total duration of all chats is {totalTime} seconds"

#Dev's chat session UI code
def sessionUI(choice,n):
    #fullStat = initCSV() #calls the initCSV() function and sets the return value to fullStat
    checkFS = re.compile("^SUMMARY") #creates a checkFS regex
    checkOS = re.compile("^CHAT SUMMARY") #creates a checkOS regex
    checkOC = re.compile("^SHOW CHAT") #creates a checkOC regex
    print(choice,n)
    choice = choice.upper() #makes the input all uppercase
    if (checkFS.search(choice)): #checks to see if the checkFS matches the input
        return getAllChatSummary()
    elif (checkOS.search(choice)): #checks to see if the checkOS matches the input
        session = choice[:len(choice)] #finds out the number from the input
        return summary(n) #calls the summary function
    elif (checkOC.search(choice)): #checks to see if the checkOC matches the input
        session = choice[:len(choice)] #finds out the number from the input
        return showchat(n) #calls the showchat function
    else:
        #prints this statement if none of the regex match
        return "Please only enter one of the 4 options."