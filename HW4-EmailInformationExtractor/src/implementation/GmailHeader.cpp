#include <iostream>
#include <string>
#include <regex>
#include "..\headers\GmailHeader.h"
using namespace std;

//Creates a Gmail Header and combines the default parts with the generic parts
GmailEmailHeader::GmailEmailHeader(string header)
{
    BaseEmailHeader();
    combinedParts.insert(combinedParts.begin(), parts.begin(), parts.end());
    combinedParts.insert(combinedParts.begin(), commonParts.begin(), commonParts.end());
    this->header = header;
}

GmailEmailHeader::~GmailEmailHeader()
{}
//Calls the parent method but expands the parts to include Gmail's.
string GmailEmailHeader::getPart(string part)
{    
    return BaseEmailHeader::getPart(part,combinedParts);
}