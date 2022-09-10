from typing import List
from algostr.sorting_algos.insertion_sort import insertionSort
from algostr.sorting_algos.selection_sort import selection_sort
from algostr.sorting_algos.shell_sort import shell_sort
from algostr.sorting_algos.heap_sort import heap_sort
from algostr.utils.dict_to_csv import write_dict_to_csv, visualize_graph
from random import shuffle

# Create a list from 1 to 1000 steps of 2
TEST_CASES = [list(range(1, 2000, 1)),
              list(range(1, 4000, 1)),
              list(range(1, 6000, 1)),
              list(range(1, 7000, 1)),
              list(range(1, 8000, 1)),
              list(range(1, 9000, 1)),
              list(range(1, 10000, 1)),
              list(range(1, 20000, 1))
              ]


def shuffle_arrs():
    
    for _ in range(0, 2):
        for case in TEST_CASES:
            shuffle(case)

def max_value(arr: List[dict], key: str):
    max_value = 0
    for item in arr:
        print(item)
        if item[key] > max_value:
            max_value = item[key]
    return max_value
    

def main():

    results_insertion_sort = []
    results_selection_sort = []
    results_shell_sort = []
    results_heap_sort = []
    
    shuffle_arrs()
    for case in TEST_CASES:
        results_insertion_sort.append(insertionSort(case))
        
    shuffle_arrs()
    for case in TEST_CASES:
        results_selection_sort.append(selection_sort(case))
        
    shuffle_arrs()
    for case in TEST_CASES:
        results_shell_sort.append(shell_sort(case))
        
    shuffle_arrs()
    for case in TEST_CASES:
        results_heap_sort.append(heap_sort(case))
            
    write_dict_to_csv(results_insertion_sort, 'insertion_sort.csv')
    
    
    
    results = [ 
        {
            'results': results_insertion_sort,
            'title': 'Insertion Sort',
            'options': {
                'x_axis': 23000,  
                'y_axis': 4000,   
                'x_key': 'n_elements',  
                'y_key': 'execution_time',  
                'title': 'Insertion Sort', 
                'x_label': 'n elements',
                'y_label': 'execution time (ms)'
            }
        },
        {
            'results': results_selection_sort,
            'title': 'Selection Sort',
            'options': {
                'x_axis': 25000,  
                'y_axis': 1000,   
                'x_key': 'n_elements',  
                'y_key': 'execution_time',  
                'title': 'Selection Sort', 
                'x_label': 'n elements',
                'y_label': 'execution time (ms)'
            }
        },
        {
            'results': results_shell_sort,
            'title': 'Shell Sort',
            'options': {
                'x_axis': 25000,  
                'y_axis': 100,   
                'x_key': 'n_elements',  
                'y_key': 'execution_time',  
                'title': 'Shell Sort', 
                'x_label': 'n elements',
                'y_label': 'execution time (ms)'
            }
        },
        {
            'results': results_heap_sort,
            'title': 'Heap sort',
            'options': {
                'x_axis': 25000,  
                'y_axis': 100,   
                'x_key': 'n_elements',  
                'y_key': 'execution_time',  
                'title': 'Heap sort', 
                'x_label': 'n elements',
                'y_label': 'execution time (ms)'
            }
        }
    ]
    
    for result in results:
        
        options = {
                'x_axis': max_value(result['results'], 'n_elements') + 200,  
                'y_axis': max_value(result['results'], 'execution_time') + 200,   
                'x_key': 'n_elements',  
                'y_key': 'execution_time',  
                'title': result['title'], 
                'x_label': 'n elements',
                'y_label': 'execution time (ms)'
            }
        
        print(result['title'])
        print(result['results'])
        
        visualize_graph(result['results'], options)
        
if __name__ == '__main__':
    main()