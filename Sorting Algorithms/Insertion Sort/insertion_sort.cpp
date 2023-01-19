
#include <iostream>
#include <cstdlib>


const int maxValue = 100;
const int testArraySize = 25;


void InsertionSort(int array[], int arraySize){
    int key;
    for (int i = 0; i < arraySize - 1; i++) {
        key = array[i + 1];  // value of index of the current key, i is the key before
        while (i >= 0 && array[i] > key)  // so long as i is valid index, loop until prior index's value is smaller
        {
            array[i + 1] = array[i];
            i--;
        }
        array[i + 1] = key;
    }
}


void ReverseInsertionSort(int array[], int arraySize){
    int key;
    for (int i = 0; i < arraySize - 1; i++) {
        key = array[i + 1];  // value of index of the current key, i is the key before
        while (i >= 0 && array[i] < key)  // so long as i is valid index, loop until prior index's value is greater
        {
            array[i + 1] = array[i];
            i--;
        }
        array[i + 1] = key;
    }
}


int Checksum(int array[], int arraySize){
    int checksum = 0;
    for (int i = 0; i < arraySize; i++) {
        checksum += array[i];
    }
    return checksum;
}


int main(){

    int testArray[testArraySize];    
    int arraySize = sizeof(testArray) / sizeof(int);
    for (int i = 0; i < arraySize; i++) {
        // srand(51 * 7 * i * i);  // Used to try different random seeds
        testArray[i] = rand() % maxValue;
    }
    
    int sortedArray[testArraySize];
    //DuplicateArray(testArray, sortedArray, arraySize);
    std::copy(std::begin(testArray), std::end(testArray), std::begin(sortedArray));
    InsertionSort(sortedArray, arraySize);

    int reversedArray[testArraySize];
    std::copy(std::begin(testArray), std::end(testArray), std::begin(reversedArray));
    ReverseInsertionSort(reversedArray, arraySize);


    std::cout << "Original List:         " << "[";
    for (int i = 0; i < arraySize - 1; i++) {
        std::cout << testArray[i] << ", ";
    }
    std::cout << testArray[arraySize - 1] << "]" << std::endl;

    std::cout << "Sorted List:           " << "[";
    for (int i = 0; i < arraySize - 1; i++) {
        std::cout << sortedArray[i] << ", ";
    }
    std::cout << sortedArray[arraySize - 1] << "]" << std::endl;

    std::cout << "Reverse Sorted List:   " << "[";
    for (int i = 0; i < arraySize - 1; i++) {
        std::cout << reversedArray[i] << ", ";
    }
    std::cout << reversedArray[arraySize - 1] << "]" << std::endl;


    std::cout << "Original List Checksum:         " << Checksum(testArray, arraySize) << std::endl;
    std::cout << "Sorted List Checksum:           " << Checksum(sortedArray, arraySize) << std::endl;
    std::cout << "Reverse Sorted List Checksum:   " << Checksum(reversedArray, arraySize) << std::endl;

}
