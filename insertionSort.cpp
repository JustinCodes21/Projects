#include <iostream>
#include <cstdlib>
using namespace std;

int* insertionSort(int arr[], int size){ //O(N^2)

    for(int i = 1; i < size; i++){
        if(arr[i] < arr[i-1]){
            int temp = arr[i-1];
            arr[i-1] = arr[i];
            arr[i] = temp;
            for(int j = i; j > 0; j--){
                if(arr[j] < arr[j-1]){
                    int temp = arr[j-1];
                    arr[j-1] = arr[j];
                    arr[j] = temp;
                }
            }
        }
    }

    return arr;
}

int main(){

    int myArray[20] = {};
    int size = sizeof(myArray)/sizeof(myArray[0]);
    int* sortedArray;
    srand((unsigned) time(NULL));

    for(int i = 0; i < size; i++){
        int random = 1 + (rand() % 100);
        myArray[i] = random;
    }
    
    cout << "\nUnsorted array: [";
    for(int i = 0; i < size; i++){
        if(i + 1 == size){
            cout << myArray[i];
            break;
        }
        cout << myArray[i] << ", ";
    }
    cout << "]";

    sortedArray = insertionSort(myArray, size);
    
    cout << "\nSorted array: [";
    for(int i = 0; i < size; i++){
        if(i + 1 == size){
            cout << *(sortedArray + i);
            break;
        }
        cout  << *(sortedArray + i) << ", ";
    }
    cout << "]\n";

    return 0;
}