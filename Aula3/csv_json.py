import csv
import pandas as pd

with open('avengers.csv', 'r') as csvfile:
    for x in csv.reader(csvfile, delimiter=','):
        print(x)
    