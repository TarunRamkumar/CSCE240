#@author Tarun
#contains the command line 
import argparse
import os
import csv
#Opens the chat_statistics csv and gets an overall summary of all chats
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

def getChatSummary(chatNum):
    #If the chat is 0, then it returns an error
    if chatNum == 0:
        return "ERROR: Invalid chat_session number. Please try again."
    with open("..\\data\\chat_statistics.csv","r") as logFile:
        log = csv.reader(logFile)
        i = 0
        for row in log:
            i+=1
            #Gets the next chatNum because rows start at 2 while chatnums start at 1
            if(chatNum+1 == i):
                return f"Chat {i-1} has {row[3]} user inputs and {row[4]} system responses, with a total session time of {row[2]} seconds"
mainParser = argparse.ArgumentParser(description="")

#adding commands

subparsers = mainParser.add_subparsers(dest="command",help="Available commands")

#summary command
summary = subparsers.add_parser("summary", help="Shows a summary of all chat sessions, or a selected one")
#Optional argument to specify chat
summary.add_argument("-c", "--chat", type=int, help="Choose a specific chat session to show summary of", required=False)

#showchat command 
showChat = subparsers.add_parser("showchat",help="Displays the desired chat session")
showChat.add_argument("-c","--chat",type=int,help="Chat session to show",required=True)

#parsing arguments
args = mainParser.parse_args()

with open("..//data//chat_statistics.csv","r",encoding="utf-8"):
    #Gets the number of sessions 
    sessionFiles = os.listdir("..\\data\\chat_sessions")
    #Logic for showchat command
    if args.command == "showchat":
        #Checks to see if valid chat value
        if args.chat and int(args.chat) <= len(sessionFiles):
            chatSession = sessionFiles[args.chat-1]
            #Special characters not parsable with utf-8, thus had to encode with cp1252
            with open(os.path.join("..\\data\\chat_sessions",chatSession),"r",encoding="cp1252") as file:
                for line in file:
                    print(line)
        elif args.chat and int(args.chat) > len(sessionFiles):
            print(f"ERROR: There are only {len(sessionFiles)} chat sessions. Please enter a valid number.")
    #Logic for summary command 
    elif args.command == "summary":
        if args.chat and int(args.chat) <= len(sessionFiles):
            print(getChatSummary(int(args.chat)))
        elif args.chat and int(args.chat) > len(sessionFiles):
            print(f"ERROR: There are only {len(sessionFiles)} chat sessions. Please enter a valid number.")
        #If no arguments are specified, gets the overall chat summary
        else:
            print(getAllChatSummary())
            