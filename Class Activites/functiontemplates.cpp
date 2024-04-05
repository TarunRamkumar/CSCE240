#include <iostream>
#include <fstream>
#include <chrono>
#include <vector>
using namespace std;

template <class A>
class SingleClassTemplate
{
    private:
        A a;
    
    public:
        SingleClassTemplate(A aa) : a(aa)
        {}
        void printValues()
        {
            cout << print(a);
        }
};
class Circle
{
    public: 
        Circle()
        {

        }
        string print()
        {
            cout << "***";
        }
};

class Line
{
    public: 
        Line()
        {
            
        }
        string print()
        {
            cout << "_____";
        }
};

class Rectangle
{
    public: 
        Rectangle()
        {
            
        }
        string print()
        {
            cout << "***";
        }
};

int main()
{
    


    return 0;
}