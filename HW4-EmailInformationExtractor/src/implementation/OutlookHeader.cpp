#include <iostream>
#include <string>
#include <regex>
#include "..\headers\OutlookHeader.h"
using namespace std;

//Calls parent constructor and then adds its own parts to the default.
OutlookEmailHeader::OutlookEmailHeader(string header)
{
    BaseEmailHeader();
    combinedParts.insert(combinedParts.begin(), parts.begin(), parts.end());
    combinedParts.insert(combinedParts.begin(), commonParts.begin(), commonParts.end());

    this->header = header;
}

OutlookEmailHeader::~OutlookEmailHeader()
{}


//Calls the parent method but expands the parts to include Outlook's.
string OutlookEmailHeader::getPart(string part)
{
    return BaseEmailHeader::getPart(part,combinedParts);
}