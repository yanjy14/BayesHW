# BayesHW Report
2017Spring
##数据分析
**_Age：_** 17~90 7种 index = 0
```
0.17-27
1.28-37
2.38-47
3.48-57
4.58-67
5.68-77
6.78-90
```

**_Workclass：_** 8种 index = 1
```
0.Private
1.Self-emp-not-inc
2.Self-emp-inc
3.Federal-gov
4.Local-gov
5.State-gov
6.Without-pay
7.Never-worked
```
**_fnlwgt：_**final analysis weights **continuous** index = 2

**_education：_**与education_num对应，不再专门处理  index = 3

**_education-num：_** 1~16 16种 index = 4

**_martial-status：_** 7种 index= 5
```
1.Married-civ-spouse
2.Divorced
3.Never-married
4.Separated
5.Widowed
6.Married-spouse-absent
7.Married-AF-spouse
```
**_occupation：_**职业 14种 index = 6
```
1.ch-support
2.Craft-repair
3.Other-service
4.Sales
5.Exec-managerial
6.Prof-specialty
7.Handlers-cleaners
8.Machine-op-inspct
9.Adm-clerical
10.Farming-fishing
11.Transport-moving
12.Priv-house-serv
13.Protective-serv
14.Armed-Forces
```
**_relationship：_** 关系 6种 index = 7
```
1.Wife
2.Own-child
3.Husband
4.Not-in-family
5.Other-relative
6.Unmarried
```
**_race：_**种族 5种 index = 8
```
1.White
2.Asian-Pac-Islander
3.Amer-Indian-Eskimo
4.Other
5.Black
```
**_sex：_**性别 2种 index = 9
```
1.Female
2.Male
```
**_capital-gain：_** continuous. index = 10

**_capital-loss：_** continuous. index = 11

**_hours-per-week：_** continuous.1-99 index = 12

**_native-country：_** 41 种 index = 13
```
1.United-States
2.Cambodia
3.England
4.Puerto-Rico
5.Canada
6.Germany
7.Outlying-US(Guam-USVI-etc)
8.India
9.Japan
10.Greece
11.South
12.China
13.Cuba
14.Iran
15.Honduras
16.Philippines
17.Italy
18.Poland
19.Jamaica
20.Vietnam
21.Mexico
22.Portugal
23.Ireland
24.France
25.Dominican-Republic
26.Laos
27.Ecuador
28.Taiwan
29.Haiti
30.Columbia
31.Hungary
32.Guatemala
33.Nicaragua
34.Scotland
35.Thailand
36.Yugoslavia
37.El-Salvador
38.Trinadad&Tobago
39.Peru
40.Hong
41.Holand-Netherlands
```

##朴素贝叶斯分类器实现
###编程语言
		Python
###程序设计
Bayes.py 和 Analysis.py
Bayes.py中采集训练数据，拿到并且处理完数据后进行测试。此处将训练与测试的文件名后缀改为.csv，易于读取处理
```
def loadCsv(filename): #读训练集数据
    lines = csv.reader(open(filename,"rb"))
    dataset = list(lines)
    return dataset
```
```
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
        else:
            print 'bug '
        #print ('p0 : {0}  p1 : {1}').format(p0,p1)
        total = len(testset)
    print ('aimed : {0} total : {1} radio: {2}').format(aimed,total,float(aimed)/total)
```

Analysis.py中处理各项特征， 得到概率分布 , 以age处理为例
其中舍弃了一些特征，并非所有特征对于结果都有好处，有些特征会产生干扰，使结果正确率下降
```
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
        res0[i] = res0[i] /income[0]
    for i in range(len(res1)):
        res1[i] = res1[i] /income[1]
    res = [res0, res1]
    return res
```
##Issue1:训练集大小的影响
**5%训练集随机抽样，结果如下**
```
1.train_size: 1629
test_aimed : 13005 test_total : 16281 ratio: 0.798783858485
2.train_size: 1629
test_aimed : 12929 test_total : 16281 ratio: 0.79411584055
3.train_size: 1629
test_aimed : 13327 test_total : 16281 ratio: 0.818561513421
4.train_size: 1629
test_aimed : 13182 test_total : 16281 ratio: 0.809655426571
5.train_size: 1629
test_aimed : 13009 test_total : 16281 ratio: 0.79902954364
```
最大精度：81.8%； 最小精度：79.4%；平均精度：80.36%

**50%训练集随机抽样，结果如下**
```
1.train_size: 16281
test_aimed : 13474 test_total : 16281 ratio: 0.827590442847
2.train_size: 16281
test_aimed : 13439 test_total : 16281 ratio: 0.825440697746
3.train_size: 16281
test_aimed : 13426 test_total : 16281 ratio: 0.824642220994
4.train_size: 16281
test_aimed : 13445 test_total : 16281 ratio: 0.825809225478
5.train_size: 16281
test_aimed : 13433 test_total : 16281 ratio: 0.825072170014
```
最大精度：82.7%； 最小精度：82.4%；平均精度：82.52%

**100%训练集，结果如下**
```
train_size: 32561
test_aimed : 13519 test_total : 16281 ratio: 0.830354400835
```
精度为83.04%

##Issue2:零概率处理
所谓零概率问题，就是计算实例概率是，如果某个分量在训练集中没出现过，会导致整个实例的概率计算结果为0，这是不合理的。
零概率问题解决采用拉普拉斯平滑算法,取 a = 1，该处理方式效果十分不错
平滑前 5%训练集精度如下
```
1.train_size: 1629
aimed : 11577 total : 16281 ratio: 0.711074258338
2.train_size: 1629
test_aimed : 11556 test_total : 16281 ratio: 0.709784411277
3.train_size: 1629
test_aimed : 11504 test_total : 16281 ratio: 0.706590504269
```
平滑后
```
1.train_size: 1629
test_aimed : 13005 test_total : 16281 ratio: 0.798783858485
2.train_size: 1629
test_aimed : 12929 test_total : 16281 ratio: 0.79411584055
3.train_size: 1629
test_aimed : 13327 test_total : 16281 ratio: 0.818561513421
```
平滑对精度提升大约8%，这是在5%训练集的情况下。训练集比例上升时，提升幅度下降，但依然有提升。

##Issue3:连续和缺失属性
连续属性的处理：根据实际情况合理分段，例如年龄 17-90 每10岁一段分了7段。具体分法见**数据分析**
缺失属性的处理：舍弃缺失属性，朴素贝叶斯分类器默认不同特征间独立，故而某些缺失属性对整体影响很小，舍弃对精度影响不大



