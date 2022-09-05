import time

def is_sorted(arr):
    for i in range(len(arr)-1):
        if (arr[i] > arr[i+1]):
            return False
    return True

def bogosort(arr):
    pass

if __name__ == "__main__":
    arr = (3, 4, 1, 5, 2)
    arr2 = (1, 2, 3, 4, 5)
    # bogosort(arr)