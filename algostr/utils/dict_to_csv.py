from typing import List, Dict
from os import remove
import matplotlib.pyplot as plt
import csv

def visualize_graph(filename):
    x = []
    y = []
    
    with open(filename, 'r') as file:
        
        # Save plots withouth the header
        
        plots = csv.reader(file, delimiter=',')
        
        plots = [plot for plot in plots if plot[0] != 'execution_time']
        
        for row in plots:
            print(row)
            x.append(float(row[0]))
            y.append(int(row[1]))

        plt.bar(x, y, color = 'y', width=0.5, label = 'Execution time')
        plt.xlabel('Execution time')
        plt.ylabel('Number of elements')
        
        plt.title('Insertion sort')
        plt.legend()
        plt.show()

def write_dict_to_csv(dicts: List[Dict], filename):
    
    # Delete the file if it exists
    try:
        remove(filename)
    except OSError:
        pass
    
    header = dicts[0].keys()
    
    with open(filename, 'a+') as file:
        writer = csv.DictWriter(file, header)
        writer.writeheader()
        writer.writerows(dicts)