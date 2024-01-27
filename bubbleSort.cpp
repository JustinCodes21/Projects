#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <ctime>
#include <iomanip>
using namespace std;

int* bubbleSort(int arr[], int size);
void swapElements(int* leftElement , int* rightElement);

int main()
{
    int myArray[10] = {};
    int size = sizeof(myArray)/sizeof(myArray[0]);
    int* sortedArray;
    clock_t start;
    clock_t end;
    srand((unsigned) time(NULL));

    for(int i = 0; i < size; i++){
        int random = rand();
        int randomNumberInRange = random % 100;
        myArray[i] = randomNumberInRange;
    }
    
    cout << "\n\t\t----Bubble Sort Algorithm----" << endl << endl;
    cout << "Unsorted array: [";
    for(int i = 0; i < size; i++){
        if(i + 1 == size){
            cout << myArray[i];
            break;
        }
        cout << myArray[i] << ", ";
    }
    cout << "]";

    start = clock();
    sortedArray = bubbleSort(myArray, size);
    end = clock();
    
    double elapsedTime = static_cast<double>(end - start) / CLOCKS_PER_SEC;
    cout << "\nSorted array:   [";
    for(int i = 0; i < size; i++){
        if(i + 1 == size){
            cout << *(sortedArray + i);
            break;
        }
        cout  << *(sortedArray + i) << ", ";
    }
    
    cout << "]\n";
    cout << "Elapsed time: " << fixed << setprecision(3) << elapsedTime << " seconds" << endl;
    cout << "--------------------------------------------------------------------------------" << endl;
    cout << "Worst case:   O(n" << char(253)  <<")" << endl;
    cout << "Average case: " << (char)233 << "(n" << char(253)  <<")" << endl;
    cout << "Best case:    " << (char)234 << "(n)" << endl;

    return 0;
}

int* bubbleSort(int arr[], int size) //O(n^2)
{
    bool isSorted = true;
    for(int i = 0; i < size - 1; i++)
    {
        for(int j = 0; j < size - 1 - i; j++)
        {
            if((arr[j] > arr[j+1]))
            {
                isSorted = false;
                swapElements(&arr[j], &arr[j+1]);
            }
        }
        if(isSorted) 
        {
            cout << "\n\n----- Best case - the array is already sorted" << endl;
            return arr;
        }
    }
    return arr;
}

void swapElements(int* leftElement , int* rightElement)
{
    int temp = *rightElement;
    *rightElement = *leftElement;
    *leftElement = temp;
}