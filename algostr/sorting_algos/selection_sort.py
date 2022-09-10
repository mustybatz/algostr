from typing import List
import time

def selection_sort(arr: List[int]):
    
    start = time.time()
    
    for i in range(len(arr)):
        
        smaller = i;
        
        for j in range(i + 1, len(arr)):
            # Encontrar el menor elemento
            if arr[j] < arr[smaller]:
                smaller = j
                
        # Intercambiar el menor elemento con el elemento actual
        arr[i], arr[smaller] = arr[smaller], arr[i]
        
    end = time.time()
    
    return {
        'execution_time': (end - start) * 1000,
        'n_elements': len(arr)
    }