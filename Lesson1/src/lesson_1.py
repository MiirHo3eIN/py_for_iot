import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

"""
    This is a notebook for the first lesson of the course "Python for IoT data analysis"


    The first lesson is the introduction to pandas to import and manipulate data

    
"""




def main():
        
    # Importing data 
    # Path: Lesson1/data/temperature.csv 
    path = f"../data/tetuan.csv"
    # Importing data from a csv file
    df = pd.read_csv(path, sep=",")

    print(df.head())
    print(df.info())
    print(df.columns)
    print(df.describe())
    print(df.dtypes)
    print(len(df))


    




if __name__ == "__main__":
    main()