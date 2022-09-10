from turtle import title
from typing import List, Dict, TypedDict
from os import remove
import matplotlib.pyplot as plt
import csv

class GraphOptions(TypedDict):
    x_axis: int # max value of x axis 
    y_axis: int # max value of y axis 
    x_key: str # key of x axis
    y_key: str # key of y axis
    title: str # title of graph
    x_label: str
    y_label: str
    

def visualize_graph(data: List[Dict], options: GraphOptions):
    x = []
    y = []
    
    x_key = options['x_key']
    y_key = options['y_key']
    
    for dict in data:
        x.append(dict[x_key])
        y.append(dict[y_key])
    
    plt.axis([1600, options['x_axis'], 0, options['y_axis']])
    plt.xlabel(options['x_label'])
    plt.ylabel(options['y_label'])
    plt.title(options['title'])
    plt.grid(True)
    plt.bar(x, y, color = 'blue', width=600)
    plt.show()

def write_dict_to_csv(dicts: List[Dict], filename):
    
    # Delete the file if it exists
    try:
        remove(filename)
    except OSError:
        pass
    
    header = dicts[0].keys()
    
    with open(filename, 'a', newline='') as file:
        writer = csv.DictWriter(file, header)
        writer.writerows(dicts)