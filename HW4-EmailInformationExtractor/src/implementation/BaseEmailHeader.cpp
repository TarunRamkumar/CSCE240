#include <iostream>
#include <string>
#include <regex>
#include "..\headers\BaseEmailHeader.h"
using namespace std;

//Default constructor for children
BaseEmailHeader::BaseEmailHeader()
{

}
//Creates a new base email and sets the header 
BaseEmailHeader::BaseEmailHeader(string header)
{
    
    this->header = header;
}

BaseEmailHeader::~BaseEmailHeader()
{

}
//Returns the common parts
vector<string> BaseEmailHeader::getCommonParts()
{
    return this->commonParts;
}
//Returns the combined parts, empty for base class
vector<string> BaseEmailHeader::getCombinedParts()
{
    return this->combinedParts;
}
//Helper method to make a string lowercase
string toLowerCase(string input)
{
    string output = "";
    for(char c : input)
        output += tolower(c);
    return output;
}
//Gets the desired part of the email
string BaseEmailHeader::getPart(string part, vector<string> parts)
{
    
    //Loops through each part to check if the given part is valid
    for(long long unsigned int i = 0; i < parts.size(); i++)
    {
        if(toLowerCase(part).compare(toLowerCase(parts[i])) == 0)
        {
           //Code segment finds the target part within the header string provided
           string targetPart = parts[i];
           std::size_t start = toLowerCase(header).find(toLowerCase(targetPart)+": ");
           if(start == string::npos)
                return "Could not find part in string.";
            
           //Finds the position of the next closest part within the header
           string nextPart = parts[0];
           std::size_t end = header.length();
           std::size_t end2 = 0;
           std::size_t currentPos = 0;
           for(size_t j = 0; j < parts.size();j++)
           {
                
                if(nextPart != targetPart)
                {
                    currentPos = toLowerCase(header).find(toLowerCase(parts[j])+": ",end2);
                    end2 = currentPos;
                    if(currentPos != string::npos && currentPos > start && currentPos < end)
                    {
                        end = currentPos;
                        nextPart = parts[j];
                    }
                } 
           }
           //Returns the substring from the desired part, ending at the start of the next closest part. 
           return header.substr(start,end-start);
          
         }
    }
    return "Error: Part not found within header. Please make sure the part you are searching for matches the valid parts provided.";

}






