#ifndef GMAILEMAILHEADER_H_
#define GMAILEMAILHEADER_H_

#include <iostream>
#include <string>
#include "BaseEmailHeader.h"

using namespace std;

class GmailEmailHeader: public BaseEmailHeader {

    private:
        const vector<string> parts = {"Delivered-To", "X-Google-Smtp-Source", "Reply-To", "Message-Index", "MIME-Version" };
    public:
        GmailEmailHeader(string header);
        string getPart(string part);
        virtual ~GmailEmailHeader();

};





#endif /*GMAILEMAILHEADER_H_*/
