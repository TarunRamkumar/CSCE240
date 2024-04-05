#include <iostream>
using namespace std;

int main()
{
    // int list[10];
    // int *p = list;

    // delete[] p;

    // int *j = new int[10];
    // int *k = j;

    int *list = new int[10];
    delete[] list;

    int x = list[2];
    cout << x;

    return 0;
}