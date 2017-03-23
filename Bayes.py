# -*- coding: utf-8 -*-
import csv
import random
from Analysis import *

def loadCsv(filename):#读训练集数据
    lines = csv.reader(open(filename,"rb"))
    dataset = list(lines)
    return dataset

if __name__ == '__main__':
    trainfile = 'train.csv'
    dataset_total = loadCsv(trainfile) #提取训练集数据
    trian_size = len(dataset_total)
    testfile = 'test.csv'
    testset = loadCsv(testfile)
    train_ratio = 1
    dataset = []
    while len(dataset)<=trian_size*train_ratio:
        if train_ratio == 1:
            dataset = dataset_total
            break
        t = random.randint(0,trian_size-1)
        dataset.append(dataset_total[t])
    total = len(dataset)
    print ('train_size: {0}').format(total)
    income = analysisincome(dataset)
    workres = analysisWorkclass(dataset,income)
    ageres = analysisage(dataset,income)
    edures = analysisedu(dataset,income)
    occupationres = analysisopt(dataset,income)
    martial_statusres = analysismartial(dataset,income)
    fnlwgtres = -1  #- 1 表示舍弃该特征
    education = -1
    relationshipres = -1
    raceres = -1
    sexres = -1
    captialgres = -1
    captiallres = -1
    hpwres = -1
    ncres = -1
    pres = [ageres,workres,fnlwgtres,education,edures,martial_statusres,occupationres,relationshipres,raceres,sexres,captialgres,captiallres,hpwres,ncres] # 特征概率列表
    income[0] = income[0]/total
    income[1] = income[1]/total
    aimed = 0#开始测试
    for i in range(len(testset)):
        lines = testset[i]
        p0 = income[0]
        p1 = income[1]
        info = analysislines(lines)
        for i in range(len(info)):
            if pres[i] != -1:
                p0 = p0 * pres[i][0][int(info[i])]
                p1 = p1 * pres[i][1][int(info[i])]
        if p0<p1:
            if lines[len(lines)-1] == '>50K.':
                aimed += 1
        elif p0>p1:
            if lines[len(lines)-1] == '<=50K.':
                aimed += 1
        total = len(testset)
    print ('test_aimed : {0} test_total : {1} ratio: {2}').format(aimed,total,float(aimed)/total)