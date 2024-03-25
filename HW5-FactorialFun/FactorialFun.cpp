#include <cmath>
#include <string>
#include <chrono>
#include <iostream>
using namespace std;

int factorial(int num)
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

int combination(int number, int setsize)
{
    int r = min(number,setsize);
    int n = max(number,setsize);

    return 
              factorial(n) 
                  / 
    (factorial(r) * factorial(n-r));
}
void factorialTime(int a)
{
    
    const auto start = std::chrono::steady_clock::now();
    int fact = factorial(a);
    const auto end = std::chrono::steady_clock::now();
    const std::chrono::duration<long double> elapsedTime{end-start};
    std::cout <<"Factorial of " << a << "= "<<fact<< "\nElapsed Time: "<< elapsedTime.count()<<"\n";
}

void combinationTime(int a, int b)
{
    const auto start = std::chrono::steady_clock::now();
    int combo = combination(a,b);
    const auto end = std::chrono::steady_clock::now();
    const std::chrono::duration<long double> elapsedTime{end-start};
    std::cout <<"Combination of " << a << " and "<<b<<" is "<<combo<< "\nElapsed Time: "<< elapsedTime.count()<<"\n";
}
string toLower(string input)
{
    string output = "";
    for(char c : input)
        output += tolower(c);
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
        if(toLower(response) == "quit" || toLower(response) == "q")
        {
            run = false;
            cout << "Have a great day!";
            return 0;
        }
        if(isdigit(response[0]))
        {
            a = response[0]-48;
        }
        if (cin.peek() != '\n') {
            cin >> b;
            if (cin.peek() != '\n') {
                cin >> compare;
            }
        }
        else{
            factorialTime(a);
            continue;
        }
        if(compare !="compare")
        {
            combinationTime(a,b);
            continue;
        }
        else{
            cout <<"Comparing the factorial and combination times: \n";
            factorialTime(max(a,b));
            combinationTime(a,b);
        }

    }
}
