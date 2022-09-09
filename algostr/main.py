from algostr.sorting_algos.insertion_sort import insertionSort
from algostr.utils.dict_to_csv import write_dict_to_csv, visualize_graph

# Create a list from 1 to 1000 steps of 2
TEST_CASES = [list(range(1, 500, 2)),
              list(range(1, 700, 2)),
              list(range(1, 1000, 2)),
              list(range(1, 2000, 2))
              ]


def main():

    results_insertion_sort = []
    
    for case in TEST_CASES:
        results_insertion_sort.append(insertionSort(case))
        
    write_dict_to_csv(results_insertion_sort, 'insertion_sort.csv')
    visualize_graph('insertion_sort.csv')