import math
def analysisWorkclass(dataset,income):
    a = 1
    res0 = [0]*8
    res1 = [0]*8
    last = len(dataset[0])
    wclass = ['Private','elf-emp-not-inc','Self-emp-inc','Federal-gov','Local-gov','State-gov','Without-pay','Never-worked']
    for i in range(len(dataset)):
        workclass = dataset[i][a]
        for j in range(len(wclass)):
            if workclass == wclass [j]:
               if dataset[i][last-1]=='>50K.':
                   res1[j] += 1;
               else:
                   res0[j] += 1
    for i in range(len(res0)):
        res0[i] = res0[i] /income[0]
    for i in range(len(res1)):
        res1[i] = res1[i] /income[1]
    res = [res0, res1]
    return res

def analysisincome(dataset):
    income = [0]*2
    last = len(dataset[0])
    for i in range(len(dataset)):
        if dataset[i][last-1]=='>50K.':
            income[1] += 1
        else:
            income[0] += 1
    income[0] = float(income[0])
    income[1] = float(income[1])
    return income

