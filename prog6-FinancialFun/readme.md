PA6 is the combination of our entire semester's course project. This program, titled "Financial Fun", currently supports 2 10K files, Google and GM. The chatbot allows the user to search through the 10ks of Google and GM. It also allows the user to pull up statistics and older chat sessions. 

Code Organization:
    The src sub directory contains the code implementation, in this case the CLI, the file parser, file reader, and session statistics logger. 

    The doc directory contains a write-up of the coding process and instructions on usage.

    The data directory contains the relevant chat-sessions data, with the csv file containing the statistics for each session and the chat-sessions subdirectory containing a file for each chat_sessions. These files contain the entire history of the session. It also contains the 10k files and the list of stopwords. 
    
    The test directory contains the test cases the program has been tested with, excluding inbuilt error cases that come with the argsparse library