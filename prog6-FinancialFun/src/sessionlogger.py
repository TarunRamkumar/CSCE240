import csv #importing csv library
import os #importing os library
import re #importing re library

def summary(n): #prints the summary of a single chat session
    count = 0 #creates a variable named count and sets it to 0
    with open("../data/chat_statistics.csv") as f: #opens the csv file
        csvReader = csv.reader(f) #creates a csv file reader
        for line in csvReader: #loops through each line in the csv
            count += 1 #incremets count by 1
            if (line[0] == n): #checks to see if the session number in the csv file and compares it to the input value
                #prints the statement below
                print("Chat "+n+" has user asking "+line[2]+" times and system respond "+line[3]+" times. Total duration is "+line[4]+" seconds.")
    if (int(n)>=count): #checks to see if the value of input value is greater than or equal to the value of count
        #prints the statement below
        print("Error. There are only "+str(count)+" sessions. Please choose a valid number. The session numbers go from 0 to "+str(count-1)+".")
    f.close() #closes the file

def showchat(n): #prints the entire chat to the terminal
    fileName = "" #creates a fileName variable
    count = 0 #creates a variable named count and sets it to 0
    with open("../data/chat_statistics.csv") as f: #opens the csv file
        csvReader = csv.reader(f) #creates a csv file reader
        for line in csvReader: #goes through each line in the csv
            if (line[0] == n): #checks to see if the session number in the csv file and compares it to the input value
                fileName = line[1] #sets the fileName variable to the chat file variable in the csv file
            count+=1 #increments count by one
    f.close() #closes the file
    if (int(n)>=count): #checks to see if the input value is greater than or equal to the value of count
        #prints the statement below
        print("Error. There are only "+str(count)+" sessions. Please choose a valid number. The session numbers go from 0 to "+str(count-1)+".")
        return #returns so that the rest of the program does not run
    print("Chat "+n+" chat is:") #prints this statement
    with open("../data/chat_sessions/"+fileName) as f: #opens a file reader for the correct chat session file
        for line in f: #iterates through the file
            print(line) #prints the line
    f.close() #closes file reader


def initCSV(): #creates the csv file with the chat session files
    list = [] #creates an empty list
    #creates the following 4 variables and sets them equal to 0
    totalNum = 0 
    totalUserUtt = 0
    totalSysUtt = 0
    totalTime = 0
    for path in os.listdir('../data/chat_sessions'): #iterates through all the files in the chat_sessions folder
        list.append(path) #adds the file to the empty list
    with open("../data/chat_statistics.csv", 'w') as csvfile: #opens a filewriter for the csv writer
        writer = csv.writer(csvfile) #creates a csv writer using the csv library
        sessionNum = 0 #creates a variable called sessionNum and sets it to 0
        for x in list: #iterates through the list
            totalNum += 1 #increases the totalNum variable by 1
            chatfile = x #creates a chatfile variable and sets it equal to the name of current file
            userUtt = 0 #creates a userUtt variable and sets it to 0
            sysUtt = 0 #creates a sysUtt variable and sets it to 0
            time = 0 #creates a time variable and sets it to 0
            with open("../data/chat_sessions/"+x, "r") as f: #opens a file reader for the current file
                for line_i, line in enumerate(f, 1): #iterates through each line in the file
                    bot = re.compile("<System>:") #creates a regex for the bot utterances
                    user = re.compile("<User>:") #creates a regex for the user utterances
                    if (bot.search(line)): #checks to see if the bot regex is in the line
                        sysUtt += 1 #increments the sysUtt by 1
                        totalSysUtt += 1 #increments the totalSysUtt by 1
                    elif (user.search(line)): #checks to see if the user regex is in the line
                        userUtt += 1 #increments the userUtt by 1
                        totalUserUtt += 1 #increments the totalUserUtt by 1
                    elif (line.find("seconds") != -1): #checks to see if the word seconds is in the line
                        end = line.find(" seconds") #finds the index of the word seconds
                        time = line[18:end] #sets time equal to the correct substring of the line
                        totalTime += float(time) #increments the totalTime by time
            writer.writerow([sessionNum, chatfile, userUtt, sysUtt, time]) #writes a row into the csv file
            sessionNum += 1 #increments the sessionNum by 1
    csvfile.close() #closes the filewriter
    return [totalNum, totalUserUtt, totalSysUtt, totalTime] #creates a list of four variable and returns it


fullStat = initCSV() #calls the initCSV() function and sets the return value to fullStat
exit = False #creates an exit variable and sets it to False
checkFS = re.compile("^SUMMARY$") #creates a checkFS regex
checkOS = re.compile("^SHOWCHAT-SUMMARY\s[0-9]+$") #creates a checkOS regex
checkOC = re.compile("^SHOWCHAT\s[0-9]+$") #creates a checkOC regex
checkQ = re.compile("^QUIT$") #creates a checkQ regex
print("Welcome to the Session Logger!") #prints a welcome statement
while (not exit): #while loop so the program does not end after one iteration
    choice = input("Type \"summary\" for the summary of all the sessions. Type \"showchat-summary n\" to find the summary of a singular session. Type \"showchat n\" to see the full chat from a session. Type \"quit\" to end the program. (Replace n with a number)") #prompts the user
    choice = choice.upper() #makes the input all uppercase
    if (checkFS.search(choice)): #checks to see if the checkFS matches the input
        print("There are "+str(fullStat[0])+" chats to date with user asking "+str(fullStat[1])+" times and system respond "+str(fullStat[2])+" times. Total duration is "+str(fullStat[3])+" seconds.")
    elif (checkOS.search(choice)): #checks to see if the checkOS matches the input
        session = choice[17:len(choice)] #finds out the number from the input
        summary(session) #calls the summary function
    elif (checkOC.search(choice)): #checks to see if the checkOC matches the input
        session = choice[9:len(choice)] #finds out the number from the input
        showchat(session) #calls the showchat function
    elif (checkQ.search(choice)): #checks to see if the checkQ matches the input
        exit = True #sets exit to True
        break #breaks the loop 
    else:
        #prints this statement if none of the regex match
        print("Please only enter one of the 4 options.")