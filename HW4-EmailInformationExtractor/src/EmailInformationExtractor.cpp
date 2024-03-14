#include <iostream>
#include <fstream>

#include "implementation\\BaseEmailHeader.cpp";
#include "implementation\\OutlookHeader.cpp";
#include "implementation\\GmailHeader.cpp";

using namespace std;

int main()
{
    bool run = true;
    //Sets up CLI
    cout <<"Welcome to the Email Information Extractor 9000!" << endl;
    while(run)
    {
        cout << "Please provide the email you wish to analyze in the input file. Then, either press 1 to set the service to Outlook, 2 to set the service to Gmail, 3 to set it to generic, or 4 to quit" << endl;
        string input;
        string response;
        cin >> input;
        
        try {
            stoi(input);
        }
        catch(...)
        {
            cout << "Invalid input, please enter an integer" << endl;
            continue;
        }

        if(stoi(input) == 4){
            cout << "Have a great day!";
            break;
        }
        //Reads the input file to see if there is a header.
        ifstream file("input.txt");
        if(!file.is_open())
        {
            cout << "Error 404: Input File Not Found" << endl;
            continue;
        }
        //Reads the file and appends it to a string
        string header = "";
        while(file)
        {
            string line;
            getline(file,line);
            header += line+"\n";
        }

        //UI Loop

        switch(stoi(input))
        {
            //Sets the header to Outlook
            case 1:
            {
                OutlookEmailHeader outlook(header);
                cout << "List of valid parts to search for Outlook: ";
                for(string s : outlook.getCombinedParts())
                    cout << s << ", ";
                cout << "\nNow enter your desired part to search by: ";
                cin >> response;
                cout << "Results below: \n" << outlook.getPart(response);
                break;
            }
            //Sets the header to GMAIL
            case 2:
            {
                GmailEmailHeader gmail(header);
                cout << "List of valid parts to search for Gmail: ";
                for(string s : gmail.getCombinedParts())
                    cout << s << ", ";
                cout << "\nNow enter your desired part to search by: ";
                cin >> response;
                cout << "Results below: \n" << gmail.getPart(response);
                break;
            }
            //Sets the header to the default 
            case 3: 
            {
                BaseEmailHeader base(header);
                cout << "List of valid parts to search for a generic service: ";
                for(string s : base.getCombinedParts())
                    cout << s << ", ";
                cout << "\nNow enter your desired part to search by: ";
                cin >> response;
                cout << "Results below: \n" << base.getPart(response, base.getCommonParts());
                break;
            }
            //Ends program
            case 4:
            {
                cout << "Have a great day!";
                run = false;
            }
            default:
            {
                cout << "Invalid input detected, please try again.";
                break;
            }
        }
            file.close();
    }
    return 0;
}