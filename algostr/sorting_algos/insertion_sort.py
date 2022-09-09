
from logging import getLogger
from typing import List
import time

LOGGER = getLogger('algostr.sorting_algos.insertion_sort')

def insertionSort(arr: List[int]):
    
    start = time.time()
    
    for i in range(1, len(arr)):
        
        actual = arr[i]
        
        # Mover elementos que sean mayores que actual
        # a una posición adelante de su posición actual
        
        j = i - 1
        while j >= 0 and actual < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = actual
        
    end = time.time()
    
    return {
        'execution_time': end - start,
        'n_elements': len(arr)
    }
        