import random

def binarySearch(list, target): #O(logN)
    start = 0
    end = len(list) - 1

    while start <= end:
        mid = (start + end) // 2
        if list[mid] is target:
            return "Value in the list"
        elif target < list[mid]:
            end = mid - 1
        elif target > list[mid]:
            start = mid + 1
    return "Value not in the list"

while(True):
    myList = []
    for i in range(0, 10):
        r1 = random.randint(1, 20)
        myList.append(r1)

    myList.sort() #In order for binary search to work, the list must be SORTED
    number = input("\nMy list contains 10 random sorted natural numbers[1-20]. \nEnter a number to check if it is in the list: ")
    result = binarySearch(myList, int(number))

    print("")
    print(result)
    print("The list: ", myList)

    answer = input("\nWould you like to go again?(Y or N): ")
    if(answer == 'Y' or answer == 'y'):
        continue
    else:
        break