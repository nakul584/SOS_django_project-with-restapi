


from service.models import Subject
from service.utility.DataValidator import DataValidator
from .BaseService import BaseService
from django.db import connection
'''
It contains Student business logics.   
'''
class SubjectService(BaseService):
    
    def search(self,params):
        print("Page No -->",params["pageNo"])
        pageNo = (params["pageNo"]-1)*self.pageSize
        sql="select * from sos_subject where 1=1"
        val = params.get("courseName", None)
        if DataValidator.isNotNull(val):
            sql+=" and courseName = '"+val+"' "
        sql+=" limit %s,%s" 
        cursor = connection.cursor()
        print("------------->",sql,params["pageNo"],self.pageSize)
        cursor.execute(sql,[pageNo,self.pageSize])
        result=cursor.fetchall()
        columnName=("id","subjectName","subjectDescription","dob","course_ID","courseName")
        res={
            "data":[]
        }
        count=0
        for x in result:
            print({columnName[i] :  x[i] for i, _ in enumerate(x)})
            res["data"].append({columnName[i] :  x[i] for i, _ in enumerate(x)})            
        return res  


        

    def get_model(self):
        return Subject
