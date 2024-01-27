#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <ctime>
#include <iomanip>
using namespace std;

int* selectionSort(int arr[], int size);
void swapElements(int* leftElement , int* rightElement);

int main()
{
    int myArray[20] = {};
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
    
    cout << "\n\t\t----Selection Sort Algorithm----" << endl << endl;
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
    sortedArray = selectionSort(myArray, size);
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
    cout << "Best case:    " << (char)234 << "(n" << char(253) << ")" << endl;

    return 0;
}

int* selectionSort(int arr[], int size)
{
    for(int i = 0, k = 0; i < size; i++)
    {
        for(int j = k = i; j < size; j++)
        {
            if(arr[j] < arr[k])
            {
                k = j;
            }
        }
        swapElements(&arr[i], &arr[k]);
    }
    return arr;
}

void swapElements(int* ithElement, int* kthElement)
{
    int temp = *ithElement;
    *ithElement = *kthElement;
    *kthElement = temp;
}