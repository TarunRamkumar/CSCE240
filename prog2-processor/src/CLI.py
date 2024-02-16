#@author Tarun
#contains the command line 
import argparse
import FileParser

mainParser = argparse.ArgumentParser(description="")

#adding commands

subparsers = mainParser.add_subparsers(dest="command",help="Available commands")

#search command
searchCommand = subparsers.add_parser("sc", help="searches through the file")

#search command arguments
group = searchCommand.add_mutually_exclusive_group(required=True)
searchCommand.add_argument("-c", "--company", type=int, help="Choose company file to search. '1' for Google and '2' for GM", required=True)
group.add_argument("-p","--part", type=str, help="Part of the 10k to search.")
group.add_argument("-i","--item", type=str, help="Subsection of part to print")

#table of contents command
tocCommand = subparsers.add_parser("toc", help="Prints out the table of contents of the file")
tocCommand.add_argument("-c", "--company", type=int, help="Company to display toc for. '1' for Google and '2' for GM", required=True)

#prints out the entire file
allCommand = subparsers.add_parser("ac", help="Prints out the entire file")
allCommand.add_argument("-c", "--company", type=int, help="Company to display toc for. '1' for Google and '2' for GM", required=True)

#parsing arguments
args = mainParser.parse_args()

#creates two file parsers, one for each company
google = FileParser.FileParser("..\data\Google10k-4Q-2024.txt")
generalMotors = FileParser.FileParser("..\data\GeneralMotors10k-4Q-2024.txt")

google.searchParts("hi")
#processes through the arguments and gives the corresponding output
if not (args.company==1 or args.company==2):
    print("Error: Invalid company detected. Retry the command, ensuring you either input 1 or 2 for the company")

elif args.company == 1:
    if args.command == "sc":
        if args.part:
            print(google.searchParts(str(args.part)))
        elif args.item:
            print(google.searchItems(str(args.item)))
            
    elif args.command == "ac":
        print(google.getFile())
    
    elif args.command == "toc":
        print(google.tableOfContents)
     
elif args.company == 2:
    if args.command == "sp":
        if args.part:
            print(generalMotors.searchParts(str(args.part)))
        elif args.item:
            print(generalMotors.searchItems(str(args.item)))
            
    elif args.command == "ac":   
        print(generalMotors.getFile())

    elif args.command == "toc":
        print(generalMotors.tableOfContents)


