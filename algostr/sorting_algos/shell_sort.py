from typing import List
import time

def shell_sort(arr: List[int]):
    
    start = time.time()
    
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        
        for i in range(gap, n):
            
            actual = arr[i]
            j = i
            
            while j >= gap and arr[j - gap] > actual:
                arr[j] = arr[j - gap]
                j -= gap
                
            arr[j] = actual
            
        gap //= 2
        
    end = time.time()
        
    return {
        'execution_time': (end - start) * 1000,
        'n_elements': len(arr)
    }