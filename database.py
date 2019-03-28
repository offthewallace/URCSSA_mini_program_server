# coding=utf8
import pickle
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
	reload(sys)
	sys.setdefaultencoding(defaultencoding)
import pandas as pd
import re
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import json
df = pd.read_excel('db2.xlsx')
#print(df.loc(1))
courseList= df['课程名／上课学期']
professorList=df['教授姓名']
professorDict = {}
count = 0
for professor in professorList:
	professorDict[professor] = []

for professor in professorList:
	professorDict[professor].append(count)
	count+=1	
with open('dict.pkl','wb') as db_file:
	pickle.dump(professorDict,db_file)
	pickle.dump(courseList,db_file)
	pickle.dump(professorList,db_file)
df.to_pickle('db.pkl')
#pickle.dump()
dict1=df.iloc[1].to_dict()
dict2=df.iloc[2].to_dict()
#z = {**dict1, **dict2}
file1 = json.dumps(dict1.decode('utf8'))

print(z)
#print(df['教授姓名'])
