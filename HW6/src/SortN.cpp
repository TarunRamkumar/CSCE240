#include <iostream>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <chrono>
#include <string>
#include <limits>

using namespace std;

// template<typename T>
// void bubbleSort(T nums, size_t size)
// {
//     for(size_t i = 0; i < size-1; i++)
//     {
//         for(size_t j = i+1; j < size; j++)
//         {
//             if(nums[i] > nums[j])
//                 {
//                     auto temp = nums[i];
//                     nums[i] = nums[j];
//                     nums[j] = temp;
//                 }
//         }
//     }
// }
//Sorts the array based on user input
void processArray(int n,int nums[], bool sortType)
{
    //If sorttype is true, runs bubblesort in ascending order
    if(sortType)
    //bubblesort for arrays
    for(int i = 0; i < n-1; i++)
    {
        for(int j = i+1; j < n; j++)
        {
            if(nums[i] > nums[j])
                {
                    auto temp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = temp;
                }
        }
    }
    //If sorttype is false, user input is standard, and sorts using the std library method
    else
        std::sort(nums,nums + n);
}

//Creates the vector by copying the array and adding items 1-by-1
std::vector<int> processVector(int n, int arr[])
{
    std::vector<int> nums;
    for(int i = 0; i < n;i++)
    {
        nums.push_back(arr[i]);
    }
    //bubble sort for vector
    for(int i = 0; i < n-1; i++)
    {
        for(int j = i+1; j < n; j++)
        {
            if(nums[i] > nums[j])
                {
                    auto temp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = temp;
                }
        }
    }

    return nums;
}
//Compares the vector and array and checks if they are equal
string validator(vector<int> vector, int nums[], int n)
{
    //Compares 
    for(int i = 0; i < n; i++)
    {
        if(vector[i] != nums[i])
            return "false";
    }
    return "true";
}

int main()
{
        string response;
        bool sortType;
        cout << "Welcome to SortN! Enter either bubble or standard followed by an int";
        int n;
        cin >> response;
        //Checks if a number is provided
        if(cin.peek() != '\n')
            cin >> n;
        else
        {
            cout << "Invalid input. Please try again";
            return 0;
        }
        cout << n;
        if(response == "bubble" && cin.good())
            sortType = true;
        else if(response == "standard" && cin.good())
            sortType = false;
        else
        {
            cout << "Invalid input. Please try again.";
            return 0;
        }
        int nums[n];
        for(int i = 0; i < n; i++)
        {
            nums[i] = rand();
        }
        

        auto startArr = std::chrono::steady_clock::now();
        processArray(n,nums,sortType);
        auto endArr = std::chrono::steady_clock::now();
        auto elapsedTimeArr = std::chrono::duration_cast<std::chrono::microseconds>(endArr - startArr);

        auto startVect = std::chrono::steady_clock::now();
        std::vector<int> vector = processVector(n, nums);
        auto endVect = std::chrono::steady_clock::now();
        auto elapsedTimeVect = std::chrono::duration_cast<std::chrono::microseconds>(endVect - startVect);

        cout << cout.fixed<<"Time for Array: " << elapsedTimeArr.count() << " microseconds\n";
        cout << cout.fixed<<"Time for Vector: " << elapsedTimeVect.count() <<" microseconds\n";
        cout << "Validated: " << validator(vector,nums,n) << "\n"; 

        return 1;
}

