/**
 * @file OO_GeometricPropertyCalculator.h
 * @author tarunr
 * @brief 
 * @version 0.1
 * @date 2024-02-06
 * 
 * @copyright Copyright (c) 2024
 * 
 */

//Dependencies
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

//User files
#include "circle.h"
#include "rectangle.h"
#include "shape.h"
#include "triangle.h"


int main()
{
    
    fstream input("input.txt");
    fstream output("output.txt",ios::app);

    if(!input.is_open())
    {
        cout << "Error 404: File Not Found";
        return 0;
    }
    if(!output.is_open())
    {
        cout << "The file could not be opened and thus nothing was outputted. Please try again.";
        return 0;
    }

    
    bool run = true;
    while(run)
    {
        
            


    }
    cout << "Have a great day!";
    input.close();
    output.close();
    return 0;
}

std::vector<string> readFile(fstream input)
{
    std::vector<string> file;
    int i = 0;
    while(getline(input,file[i]))
    {
        i++;
    }
    return file;
}

void userInteraction(std::vector<string> file)
{
    int response;
    cout << "Press 1 to calculate areas, 2 to calculate perimeters.";
    cin >> response;
    string calc;
    if(response == 1)
        calc = "AREA";
    else if(response == 2)
        calc = "PERIMETER";
    else{
        cout <<"Invalid input, please try again";
        return;
    }

    for(int i = 0; i < file.size(); i++)
    {
        if(calc.compare("AREA") == 0)
        {
            calculateArea(file[i]);
        }
        else if(calc == "PERIMETER")
        {
            calculatePerimeter(file[i]);
        }
    }
    
}

string calculateArea(string line)
{
    string shape;
    double a,b,c;

    stringstream ss(line);
    ss >> shape >> a >> b >> c;
            if(shape == "RECTANGLE")
            {
                Rectangle rect(a,b);
                string area = to_string(rect.calculateArea());
                return shape + " Area = " + area +'\n';
            }
            else if(shape == "CIRCLE")
            {
                Circle circ(a);
                string area = to_string(circ.calculateArea());
                return shape + " Area = " + area +'\n';
            }
            else if(shape == "TRIANGLE")
            {
                Triangle tri(a,b,c);
                string area = to_string(tri.calculateArea());
                return shape + " Area = " + area +'\n';
            }
            else
            {
                cout << "Error: Invalid shape detected. Skipped line.\n";
            }
}
string calculatePerimeter(string line)
{
    string shape;
    double a,b,c;

    stringstream ss(line);
    ss >> shape >> a >> b >> c;
            if(shape == "RECTANGLE")
            {
                Rectangle rect(a,b);
                string perimeter = to_string(rect.calculatePerimeter());
                return shape + " Area = " + perimeter +'\n';
            }
            else if(shape == "CIRCLE")
            {
                Circle circ(a);
                string perimeter = to_string(circ.calculatePerimeter());
                return shape + " Area = " + perimeter +'\n';
            }
            else if(shape == "TRIANGLE")
            {
                Triangle tri(a,b,c);
                string perimeter = to_string(tri.calculatePerimeter());
                return shape + " Area = " + perimeter +'\n';
            }
            else
            {
                cout << "Error: Invalid shape detected. Skipped line.\n";
            }
}