#include <iostream>
#include <fstream>
#include <cctype>
using namespace std;

int main()
{
    
    string operation;
    string firstNum;
    string secondNum;
    int answer;
    fstream input("input.txt");
    if(!input.is_open())
    {
        cout << "Error 404: File Not Found";
        return 0;
    }
    getline(input, operation);
    getline(input, firstNum);
    getline(input,secondNum);

    if(operation == "add")
    {
        answer = stoi(firstNum) + stoi(secondNum);
        operation = "addition";
    }
    else if(operation == "subtract")
    {
        answer = stoi(firstNum) - stoi(secondNum);
        operation = "subtraction";
    }
    else if(operation == "multiply")
    {
        answer = stoi(firstNum) * stoi(secondNum);
        operation = "multiplication";
    }
    else if(operation == "divide")
    {
        answer = stoi(firstNum) / stoi(secondNum);
        operation = "division";
    }

    fstream output("output.txt");
    if(!output.is_open())
    {
        cout << "The file could not be opened and thus nothing was outputted. Please try again.";
        return 0;
    }
    output << "The result of " + operation + " on " + firstNum + " and " + secondNum + " is below.\n"+ to_string(answer);
    
    output.close();
    input.close();
    return 0;
}