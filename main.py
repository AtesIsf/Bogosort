import time
from datetime import datetime
import random

def is_sorted(arr):
    for i in range(len(arr)-1):
        if (arr[i] > arr[i+1]):
            return False
    return True

def bogosort(arr):
    while (is_sorted(arr) == False):
        random.shuffle(arr)

if __name__ == "__main__":
    arr = (3, 4, 1, 5, 2)

    start = time.time()
    bogosort(arr)
    end = time.time()

    with open("logs.txt", "a") as file:
        curr_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        file.write(f"Date-time: {curr_datetime}, Elapsed time: {end-start}s\n")