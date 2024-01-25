#include<iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <cctype>
using namespace std;

int main()
{
    fstream input("input.txt");
    if(!input.is_open())
    {
        cout << "Error 404: File Not Found";
        return 0;
    }
    fstream output("output.txt");
    if(!output.is_open())
    {
        cout << "The file could not be opened and thus nothing was outputted. Please try again.";
        return 0;
    }

    string rect(double width, double height,int action);
    string circ(double radius, int action);
    string tri(double a, double b, double c, int action);
    bool run = true;
    while(run)
    {
        int response;
        cout << "Press 1 to calculate areas, 2 to calculate perimeters.";
        cin >> response;
        string calc;
        if(response == 1)
            calc = "AREA";
        else
            calc = "PERIMITER";
        string line;
        char buff;
        while(getline(input, line))
        {
            string shape;
            double a,b,c;

            stringstream ss(line);
            ss >> shape >> a >> b >> c;
            
            if(shape == "RECTANGLE")
            {

                output << shape + " " + calc + " = " + rect(a,b,response)+'\n';
            }
            else if(shape == "CIRCLE")
            {
                output << shape + " " + calc + " = " +circ(a,response)+'\n';
            }
            else if(shape == "TRIANGLE")
            {
                output << shape + " " + calc + " = " + tri(a,b,c,response)+'\n';
            }
            else
            {
                cout << "Error: Invalid shape detected. Skipped line.\n";
            }

            
        
            

        }
        cout << "Program finished, press 1 to exit, anything else to continue";
        int resp;
        cin >> resp;
        if(resp == 1)
            run = false;
    }
    cout << "Have a great day!";
    input.close();
    output.close();
    return 0;
}

string rect(double width, double height,int action)
{
    if(width == NULL || height == NULL)
        return "Not enough information to calculate";
    else if(action == 1 )
        return to_string(round(width*height*1000)/1000);
    else
        return to_string(2*width + 2*height);
}



string circ(double radius, int action)
{
    if(radius == NULL)
        return "Not enough information to calculate";
    else if(action == 1 )
        return to_string(round(M_PI * radius * radius*1000)/1000);
    else
        return to_string(round(2*M_PI*radius*1000)/1000);
    
}



string tri(double a, double b, double c, int action)
{
    if(a == NULL || b == NULL || c == NULL)
        return "Not enough information to calculate";
    else if(action == 1 )
    {
        double s = (a+b+c)/2;
        return to_string(sqrt(s*(s-a)*(s-b)*(s-c)));
    }
    else
        return to_string(a+b+c);
    
}



