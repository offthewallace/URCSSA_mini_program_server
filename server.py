# coding=utf8
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
import pandas as pd
import re
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

from flask import Flask,render_template,request,json

 
app = Flask(__name__)
dbfile= open('dict.pkl','rb')
dbfile2= open('db.pkl','rb') 
df = pd.read_pickle(dbfile2)
professorDict=pickle.load(dbfile)
courseList=pickle.load(dbfile)
professorList=pickle.load(dbfile)

@app.route('/getinfo',methods=['POST'])
def info():
    #df = pd.read_csv('db2.csv')
    df =pd.read_pickle('db.pkl')
    info = str(json.loads(request.values.get("input")))
    def hasNumbers(inputString):
        return bool(re.search(r'\d', inputString))
    if hasNumbers(info):
        course=process.extract(info, courseList, limit=1)
        courseIndex = courseList.find(course)
        res = df.iloc[courseIndex]
        return json.dumps(res.decode('utf8'))
    else:    
        res ='no Result'
        return json.dumps(res.decode('utf8'))
    
if __name__ == '__main__':
    app.run(debug=True)
