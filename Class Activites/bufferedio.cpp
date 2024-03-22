#include <iostream>
#include <fstream>
#include <chrono>
#include<vector>
using namespace std;

std::vector<string> readWithoutBuffer()
{
    fstream input("Class Activites\\GeneralMotors10k-4Q-2024.txt");
    std::vector<string> file;
    int i = 0;
    while(getline(input,file[i]))
    {
        i++;
    }
    return file;
}

std::vector<string> readWithBuffer()
{
    fstream input("Class Activites\\GeneralMotors10k-4Q-2024.txt");
    std::vector<string> file;
    int bufferSize = 1024;
    char buffer[bufferSize];
    for(int i = 0; i < bufferSize; i++)
    {
        buffer[i] = " ";
    }
    fread(buffer);
    return file;
}
int main()
{
    auto start = std::chrono::steady_clock::now();
    std::vector<string> file = readWithoutBuffer();
    auto end = std::chrono::steady_clock::now();
    auto elapsedTime = end-start;
    cout << "Time Elapsed: " << elapsedTime;

}