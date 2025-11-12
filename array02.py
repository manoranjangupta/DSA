from typing import List

def sortArray(arr: List[int]) ->int:
    arr.sort()
    return arr[-1]

if __name__ == "__main__":
    arr1=[2,4,9,6,7,21]
    print("Largest element of array is : ",sortArray(arr1))
