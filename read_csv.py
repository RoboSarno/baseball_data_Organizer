import csv
import pandas as pd

class CSV:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = []
  
       
    def create_NParray(self):
        print(self.df.values)


        
        
    def read_Csv(self):
        self.df = pd.read_csv(self.csv_path, sep=',',header=None)
                

                             
    
            
