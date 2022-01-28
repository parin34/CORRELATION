
import numpy as np
import csv

def getDataSource(data_path):
    marks = []
    days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))
    return {"x" : marks, "y": days_present}

def findCorrrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("correlation",correlation[0,1])

def setup():
    data_path ="data.csv"
    datasource = getDataSource(data_path)
    findCorrrelation(datasource)

setup()


