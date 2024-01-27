#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <ctime>
#include <iomanip>
using namespace std;

int* insertionSort(int arr[], int size);

int main()
{
    int myArray[10] = {};
    int size = sizeof(myArray)/sizeof(myArray[0]);
    int* sortedArray;
    clock_t start;
    clock_t end;
    srand((unsigned) time(NULL));

    for(int i = 0; i < size; i++){
        int random = 1 + (rand() % 100);
        myArray[i] = random;
    }

    cout << "\n\t\t----Insertion Sort Algorithm----" << endl << endl;
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
    sortedArray = insertionSort(myArray, size);
    end = clock();

    double elapsedTime = (double)(end - start) / CLOCKS_PER_SEC;
    
    cout << "\nSorted array: [";
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

int* insertionSort(int arr[], int size) //O(n^2)
{ 
    for(int i = 1; i < size; i++)
    {
        if(arr[i] < arr[i-1])
        {
            int temp = arr[i-1];
            arr[i-1] = arr[i];
            arr[i] = temp;
            for(int j = i; j > 0; j--)
            {
                if(arr[j] < arr[j-1])
                {
                    int temp = arr[j-1];
                    arr[j-1] = arr[j];
                    arr[j] = temp;
                }
            }
        }    
    }
    return arr;
}