#@author Tarun
class FileParser:
#Creates a new FileParser object
    def __init__(self,fileName):
        
        self.fileName = fileName
        #formats the file and removes any escape characters and whitespaces 
        with open(self.fileName, "r+", encoding="utf-8") as file:
            content = file.read()
            content = self.formatFile(content)
        with open(self.fileName, "w", encoding="utf-8") as file:
            file.write(content)
        self.listTOC = self.setTOC()
        self.tableOfContents = self.groupTOC(self.listTOC)
         

    def formatFile(self, content):
        formattedContent = content.replace(u'\xa0', u' ').strip()
        return formattedContent
    #Creates the table of contents, but keeps it as a list rather than a dictionary
    def setTOC(self):
        tableOfContents = []
        with open(self.fileName, "r", encoding="utf-8") as file:
            started = False
            for line in file:
                if "PART I" in line.strip():
                    started = True
                elif started and "Table of Contents" in line.strip():
                    print("done")
                    break
                elif started and not line.strip().isnumeric():
                    tableOfContents.append(line.strip())
        mergedTOC = []
        i = 0
        #Merges the items with their headings/descriptions
        while i < len(tableOfContents):
            if "Item" in tableOfContents[i]:
                mergedTOC.append(tableOfContents[i] + " " + tableOfContents[i+1])
                i+=2
            else:
                mergedTOC.append(tableOfContents[i])
                i+=1
        #return self.groupTOC(mergedTOC)
        return mergedTOC
    
    #Groups the TOC together into a dictionary, with the parts including all their children items 
    def groupTOC(self,currentTOC):
        groupedTOC = {"Part 0":[]}
        currentPart = ""
        for item in currentTOC:
            if "PART" in item:
                currentPart = item
                groupedTOC[currentPart] = []
            else:
                if currentPart:
                    groupedTOC[currentPart].append(item)
                else:
                    groupedTOC["Part 0"].append(item)
        return groupedTOC
    #Searches the file for each part, and returns the entire part
    def searchParts(self,part):
        result = ""
        
        toc = self.tableOfContents
        if part.upper() in toc.keys():
            listKeys = list(toc.keys())
            if listKeys.index(part.upper()) == len(listKeys)-1:
                nextItem = "None"
            else:
                nextItem = listKeys.pop(listKeys.index(part.upper())+1)
            with open(self.fileName, "r", encoding="utf-8") as file:
                started = False
                started2 = False
                for line in file:
                    if started2 == False and part.upper() == line.strip():
                        started2 = True
                    elif started2 and part.upper() == line.strip():
                        started = True
                    elif started and line.strip().upper() == nextItem:
                        return result
                    elif started and nextItem == "None":                        
                        result+=line
                    elif started:
                        result += line
                return result
        else:
            return part + " not found in file. Please try again with another parameter. Valid values can be found using the 'toc' command"
    
    #Searches the items within each part, and returns them individually
    def searchItems(self, item):
        result = ""
        toc = self.listTOC
        
        for string in toc:
            if(item in string):
                if toc.index(string) == len(toc) - 1:
                    nextItem = "None"
                else:
                    nextItem = toc.pop(toc.index(string)+1)
                
                with open(self.fileName, "r", encoding="utf-8") as file:
                    started = False
                    started2 = False
                    for line in file:
                        if started2 == False and item in line.strip():
                            started2 = True
                        elif started2 and item.lower() == line.strip().lower():
                            started = True
                        elif started and line.strip().lower() == nextItem.lower():
                            return result
                        elif started and nextItem == "None":
                            result+=line
                        elif started:
                            result += line
                    return result
        else:
            return item + " not found in file. Please try again with another parameter. Valid values can be found using the 'toc' command"
        
    #Gets the entire file and returns it as a string
    def getFile(self):
        result = ""
        with open(self.fileName, "r", encoding="utf-8") as file:
            for line in file:
                result += line
        return result
            
                
