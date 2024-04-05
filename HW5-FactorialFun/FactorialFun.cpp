#include <cmath>
#include <string>
#include <chrono>
#include <iostream>
using namespace std;
//Calculates the factorial value of a integer. Set to long long int to handle the extreme cases of a factorial. If the input is negative, the method just calculates the factorial of the absolute value. 
long long int factorial(int num)
{
    if(num < 1)
    {
        num *=-1;
    }
    if(num == 1 || num == 0)
    {
        return 1;
    }
    else
    {
        return num * factorial(num-1);
    }
}
//Calculates the combinations of the two numbers. Takes the min of the numbers and sets it to r, because this is a necessary condition for the formula.
int combination(int number, int setsize)
{
    int r = min(number,setsize);
    int n = max(number,setsize);

    return 
              factorial(n) 
                  / 
    (factorial(r) * factorial(n-r));
}
//Prints the time taken to run the factorial method
void factorialTime(int a)
{
    
    const auto start = std::chrono::steady_clock::now();
    long long int fact = factorial(a);
    const auto end = std::chrono::steady_clock::now();
    //Set to long double to handle extremely small numbers
    const std::chrono::duration<long double> elapsedTime{end-start};
    std::cout <<"Factorial of " << a << "= "<<fact<< "\nElapsed Time: "<< elapsedTime.count()<<"\n";
}
//Prints the time taken to calculate the combinations of the two ints.
void combinationTime(int a, int b)
{
    const auto start = std::chrono::steady_clock::now();
    int combo = combination(a,b);
    const auto end = std::chrono::steady_clock::now();
    const std::chrono::duration<long double> elapsedTime{end-start};
    std::cout <<"Combination of " << a << " and "<<b<<" is "<<combo<< "\nElapsed Time: "<< elapsedTime.count()<<"\n";
}
//Makes the input string lowercase
string toLower(string input)
{
    string output = "";
    for(char c : input)
        output += std::tolower(c);
    return output;
}
int main(){
    bool run = true;
    while(run){
        std::cout <<"Welcome to factorial fun! Input 1 number to compute a factorial, 2 numbers to compute a combination, or  2 numbers + 'compare' to compare the times for both. Type q or quit to quit. If an invalid value is detected, the combination of the default values will be computed.\n";
        int a = 0;
        int b = -1;
        string compare;
        string response;
        cin >> response;
        //Lets the user quit
        if(toLower(response) == "quit" || toLower(response) == "q")
        {
            run = false;
            cout << "Have a great day!";
            return 0;
        }
        //Sets a to the input if the input is the digit
        if(isdigit(response[0]))
        {
            //Subtracts by the ascii value of 0 (48) to compute the int value of the char
            a = response[0]-48;
        }
        else{
            continue;
        }
        //Checks to see if the cin line ends or other numbers exist
        if (cin.peek() != '\n') {
            cin >> b;
            if (cin.peek() != '\n') {
                cin >> compare;
            }
        }
        //If only one number is inputted, the factorial time is returned.
        else{
            factorialTime(a);
            continue;
        }
        //If compare is not inputted, the combination time is returned
        if(compare !="compare")
        {
            combinationTime(a,b);
            continue;
        }
        //Finally, the two times are calculated and returned.
        else{
            cout <<"Comparing the factorial and combination times: \n";
            factorialTime(max(a,b));
            combinationTime(a,b);
        }

    }
}
