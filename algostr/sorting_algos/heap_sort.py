from typing import List
import time

def heapify(arr: List, i: int):
    
    greatest = i
    l = 2 * i + 1
    r = 2 * i + 2
    
    # Si el hijo izquierdo es mayor que el padre
    # entonces el mayor es el hijo izquierdo
    if l < len(arr) and arr[i] < arr[l]:
        greatest = l
        
    # Si el hijo derecho es mayor que el padre
    # entonces el mayor es el hijo derecho
    if r < len(arr) and arr[greatest] < arr[r]:
        greatest = r
        
    # Si el mayor no es el padre
    # entonces intercambiar el mayor con el padre
    if greatest != i:
        arr[i], arr[greatest] = arr[greatest], arr[i]
        
        # Heapify el subárbol afectado
        heapify(arr, greatest)

def heap_sort(arr: List[int]):
    
    start = time.time()
    
    for i in range(len(arr) // 2 - 1 , -1 , -1):
        heapify(arr, i)
    
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i)
        
    end = time.time()
        
    return {
        'execution_time': (end - start) * 1000,
        'n_elements': len(arr)
    }