import sys
# import matplotlib
# import matplotlib.pyplot as plt
import numpy as np
from io import StringIO
from read_csv import CSV
sys.path.append('./read_csv.py')



n = CSV('./baseballdatabank/core/Appearances.csv')
n.read_Csv()
n.create_NParray()
# class graph_Types:
#     def __init__(self, name):
#         self.name = name
        
#         d = CSV('./baseballdatabank/core/Appearances.csv')
#         self.data = read_Csv()
    
#     #decides what graph is going ot be displayed based on used inputed name
#     def graph(self):
        
#     #functions that graph the data and are called in graph
    
