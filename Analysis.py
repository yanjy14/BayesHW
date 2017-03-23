import math
def analysisWorkclass(dataset,income):
    index = 1
    res0 = [0]*8
    res1 = [0]*8
    last = len(dataset[0])
    wclass = ['Private','elf-emp-not-inc','Self-emp-inc','Federal-gov','Local-gov','State-gov','Without-pay','Never-worked']
    for i in range(len(dataset)):
        workclass = dataset[i][index]
        if workclass == '?':
            continue
        for j in range(len(wclass)):
            if workclass == wclass [j]:
               if dataset[i][last-1]=='>50K.':
                   res1[j] += 1;
               else:
                   res0[j] += 1
    for i in range(len(res0)):
        res0[i] = (res0[i]+1) /(income[0]+8)
    for i in range(len(res1)):
        res1[i] = (res1[i]+1) /(income[1]+8)
    res = [res0, res1]
    return res

def analysisincome(dataset):
    income = [0]*2
    last = len(dataset[0])
    for i in range(len(dataset)):
        incomet = dataset[i][last-1]
        if incomet == '?':
            continue
        if dataset[i][last-1]=='>50K.':
            income[1] += 1
        else:
            income[0] += 1
    income[0] = float(income[0])+1
    income[1] = float(income[1])+1
    return income

def analysisage(dataset,income):
    index = 0
    res0 = [0]*7
    res1 = [0]*7
    last = len(dataset[0])
    for i in range(len(dataset)):
        if(dataset[i][index] == '?'):
            continue
        age = int(dataset[i][index])
        offset = (age-17)/10
        if offset == 7:
            offset -= 1
        if dataset[i][last - 1] == '>50K.':
            res1[offset] += 1;
        else:
            res0[offset] += 1
    for i in range(len(res0)):
        res0[i] = (res0[i]+1) /(income[0]+7)
    for i in range(len(res1)):
        res1[i] = (res1[i]+1) /(income[1]+7)
    res = [res0, res1]
    return res

def analysisedu(dataset,income):
    index = 4
    types = 16
    res0 = [0] * types
    res1 = [0] * types
    last = len(dataset[0])
    for i in range(len(dataset)):
        if dataset[i][index]=='?':
            continue
        edu_num = int(dataset[i][index])
        if dataset[i][last - 1] == '>50K.':
            res1[edu_num-1] += 1;
        else:
            res0[edu_num-1] += 1
    for i in range(len(res0)):
        res0[i] = (res0[i]+1) /(income[0]+types)
    for i in range(len(res1)):
        res1[i] = (res1[i]+1) /(income[1]+types)
    res = [res0, res1]
    return res

def analysisopt(dataset,income):
    index = 6
    types = 14
    res0 = [0] * types
    res1 = [0] * types
    last = len(dataset[0])
    occupation = ['Tech-support','Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty', 'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing', 'Transport-moving', 'Priv-house-serv', 'Protective-serv', 'Armed-Forces']
    for i in range(len(dataset)):
        opt = dataset[i][index]
        if opt=='?':
            continue
        for j in range(len(occupation)):
            if opt == occupation [j]:
                if dataset[i][last - 1] == '>50K.':
                    res1[j] += 1;
                else:
                    res0[j] += 1
    for i in range(len(res0)):
        res0[i] = (res0[i]+1) / (income[0]+types)
    for i in range(len(res1)):
        res1[i] = (res1[i]+1) / (income[1]+types)
    res = [res0, res1]
    return res

def analysismartial(dataset,income):
    index = 5
    types = 7
    res0 = [0] * types
    res1 = [0] * types
    last = len(dataset[0])
    martial_status = ['Married-civ-spouse','Divorced','Never-married','Separated','Widowed','Married-spouse-absent','Married-AF-spouse']
    for i in range(len(dataset)):
        martial_s = dataset[i][index]
        if martial_s == '?':
            continue
        for j in range(len(martial_status)):
            if martial_s == martial_status[j]:
                if dataset[i][last - 1] == '>50K.':
                    res1[j] += 1;
                else:
                    res0[j] += 1
    for i in range(len(res0)):
        res0[i] = (res0[i]+1) / (income[0]+types)
    for i in range(len(res1)):
        res1[i] = (res1[i]+1) /(income[1]+types)
    res = [res0, res1]
    return res

def analysislines(lines):
    aget = int(lines[0])
    age = (aget - 17) / 10
    if age==7:
        age = 6

    workclasst = lines[1]
    workclass = -1
    wclass = ['Private', 'elf-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Without-pay','Never-worked']
    for j in range(len(wclass)):
        if workclasst == wclass[j]:
            workclass = j
            break

    fnlwgt = -1

    education = -1

    edu_num = int(lines[4])-1

    martialt = lines[5]
    martial = -1
    martial_status = ['Married-civ-spouse', 'Divorced', 'Never-married', 'Separated', 'Widowed',
                      'Married-spouse-absent', 'Married-AF-spouse']
    for j in range(len(martial_status)):
        if martialt == martial_status[j]:
            martial = j
            break

    occuptiont = lines[6]
    occuption = -1
    occupationset= ['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty',
                  'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing', 'Transport-moving',
                  'Priv-house-serv', 'Protective-serv', 'Armed-Forces']
    for j in range(len(occupationset)):
        if occuptiont == occupationset[j]:
            occuption = j
            break

    relationship = -1

    race = -1

    sex = -1

    captial_gain = -1
    captial_loss = -1

    hours_per_week = -1

    native_country = -1

    info = [age,workclass,fnlwgt,education,edu_num,martial,occuption,relationship,race,sex,captial_gain,captial_loss,hours_per_week,native_country]
    return info




