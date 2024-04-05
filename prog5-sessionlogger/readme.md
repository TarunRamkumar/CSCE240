PA5 is a session chat logger written for the honors section of CSCE 240, by Tarun Ramkumar. The aim of this code is to save and parse through all user's chat sessions, allowing them to see relevant statistics for all sessions, or individual ones. The end goal of this program is to be combined with PA4 to create a chatbot that allows the user to parse through a company's 10k, whilst also being able to view older chat sessions and their statistics. 

Code Organization:
    The src sub directory contains the code implementation, in this case simply the CLI logic. 
    The doc directory contains a write-up of the coding process, and an explanation/help guide to the CLI interface/commands.
    The data directory contains the relevant chat-sessions data, wiht the csv file containing the statistics for each session and the chatsessions 
        subdirectory containing a file for each chat_sessions. These files contain the entire history of the session. 
    The test directory contains the test cases the program has been tested with, excluding inbuilt error cases that come with the argsparse library