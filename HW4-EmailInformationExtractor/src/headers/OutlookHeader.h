#ifndef OUTLOOKEMAILHEADER_H_
#define OUTLOOKEMAILHEADER_H_

#include <iostream>
#include <string>
#include "BaseEmailHeader.h"

using namespace std;

class OutlookEmailHeader: public BaseEmailHeader {

    private:
        const vector<string> parts = {"Authentication-Results", "CC", "Thread-Topic","Thread-Index", "Message-ID", "References", "In-Reply-To", "Accept-Language", "Content-Language", "X-MS-Has-Attach", "X-MS-Exchange-Organization-SCL"};
        
    public:
        OutlookEmailHeader(string header);
        string getPart(string part);
        virtual ~OutlookEmailHeader();

};





#endif /*OUTLOOKEMAILHEADER_H_*/
