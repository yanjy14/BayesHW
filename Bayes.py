# -*- coding: utf-8 -*-
import csv
from Analysis import *

def loadCsv(filename):#读训练集数据
    lines = csv.reader(open(filename,"rb"))
    dataset = list(lines)
    return dataset

if __name__ == '__main__':
    filename = 'debug-train.csv'
    dataset = loadCsv(filename) #提取训练集数据
    total = len(dataset)
    income = analysisincome(dataset)
    workres = analysisWorkclass(dataset,income)

    print('Loaded data file {0} with {1} rows').format(filename, len(dataset))
    print ('analysis workclass : {0}').format(workres)
    print ('income : {0}').format(income)