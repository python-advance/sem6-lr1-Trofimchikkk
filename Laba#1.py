import pandas as pd
data = pd.read_csv('titanic.csv', index_col='PassengerId')
import numpy as np

#1

sex_counts = data['Sex'].value_counts()

def sex_count(sex, data = None):
    setsex = data.value_counts()
    if sex == 'male':
        return setsex['male']
    else:
        return setsex['female']
    
male_numb = sex_count('male', data['Sex'] )
female_numb = sex_count('female', data['Sex'])
print("Ответ:" , male_numb, female_numb)

#2

embarked_counts = data['Embarked'].value_counts()
print("Ответ:" , embarked_counts['C'], embarked_counts['S'],embarked_counts['Q'])

#3

surv_counts = data['Survived'].value_counts()

def surv_count(survived, data = None):
    setsurv = data.value_counts()
    if survived == 0:
        return setsurv[0]
    else:
        return setsurv[1]
    
not_surv_numb = surv_count(0, data['Survived'])
surv_percent = 100.0 * not_surv_numb / surv_counts.sum()
print("Ответ:" ,not_surv_numb,"{:0.2f}".format(surv_percent))

#4

def get_number_of_class(rec):
    
  data = pd.read_csv(rec)
  pclass_percent1 = 100.0 * pclass_counts[1] / pclass_counts.sum()
  pclass_percent2 = 100.0 * pclass_counts[2] / pclass_counts.sum()
  pclass_percent3 = 100.0 * pclass_counts[3] / pclass_counts.sum()
  return pclass_percent1,pclass_percent2,pclass_percent3

get_number_of_class('titanic.csv')

#5

def corr_Pirson(x, y):
    
    data = pd.read_csv('titanic.csv')
    res = data[x].corr(data[y])
    return res

answer = corr_Pirson('SibSp','Parch' )
print("Ответ:", "{:0.2f}".format(answer))

#6

def corr_Pirson(x, y):
    
    data = pd.read_csv('titanic.csv')
    res = data[x].corr(data[y])
    return res

answer = corr_Pirson('Age','Survived' )
print("Ответ№6:", "{:0.2f}".format(answer))


answer1 = corr_Pirson('Pclass','Survived' )
print("Ответ:", "{:0.2f}".format(answer1))

#7

def age(data = None):
    
    age_lst = data.value_counts().index.tolist()
    return np.average(age_lst), np.median(age_lst)
age_int = age(data['Age'])

print("Ответ:",age_int)

#8

def price(data = None):
    
    price_lst = data.value_counts().index.tolist()
    return np.average(price_lst),np.median(price_lst)
price_int = price(data['Fare'])

print("Ответ:",price_int)

#9

def clean_name(name):
    s = re.search('^[^,]+, (.*)', name)
    if s:
        name = s.group(1)
    s = re.search('\(([^)]+)\)', name)
    if s:
        name = s.group(1)
    name = re.sub('(Master\. |Mr\. |Mrs\. )', '', name)
    name = name.split(' ')[0].replace('"', '')
    return name

names = data[data['Sex'] == 'male']['Name'].map(clean_name)
name_counts = names.value_counts()
print("Ответ:",name_counts.head(1).index.values[0])

#10

def clean_name(name):
    import re
    
    s = re.search('^[^,]+, (.*)', name)
    if s:
        name = s.group(1)

   
    s = re.search('\(([^)]+)\)', name)
    if s:
        name = s.group(1)
 
   
    name = re.sub('(Master\. |Mr\. |Mrs\. |Miss\. )', '', name)

   
    name = name.split(' ')[0].replace('"', '')

    return name

def get_name(dataset,sex,age):
    if (dataset is None):
        return ''
    names = dataset[data['Age'] > age]['Name'].map(clean_name)
    if (sex=='male' or sex=='female'):
        names = dataset[data['Sex'] == sex][data['Age'] > age]['Name'].map(clean_name)
    name_counts = names.value_counts()
    if(name_counts.count()>0):
        return name_counts.head(1).index.values[0]
    return ''


print('\n')

print('Мужское: '+ get_name(data,'male',15))

print('Жен: '+ get_name(data,'female',15))
