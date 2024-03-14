#ifndef BASEEMAILHEADER_H_
#define BASEEMAILHEADER_H_

#include <iostream>
#include <string>
#include <vector>
using namespace std;

class BaseEmailHeader {

    protected:
        const vector<string> commonParts = {"Received", "Content-Type", "From", "To", "Date" , "Subject","Content-Transfer-Encoding"};
        string header;
        vector<string> combinedParts;

    public:
        BaseEmailHeader();
        BaseEmailHeader(string header);
        string getPart(string part, vector<string> parts);
        vector<string> getCommonParts();
        vector<string> getCombinedParts();
        virtual ~BaseEmailHeader();

};





#endif /*BASEEMAILHEADER_H_*/

