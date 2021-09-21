from service.models import College
from service.utility.DataValidator import DataValidator
from .BaseService import BaseService
from django.db import connection

'''
It contains Role business logic's.   
'''


class CollegeService(BaseService):
    
    def get_model(self):
        return College
    def search(self, params):
        pageNo = (params["pageNo"] - 1) * self.pageSize
        sql = "select * from sos_college where 1=1"
        val = params.get("collegeName", None)
        if DataValidator.isNotNull(val):
            sql += " and collegeName = '" + val + "' "  
        sql += " limit %s,%s"
        cursor = connection.cursor()
        cursor.execute(sql, [pageNo,self.pageSize])
        resultt = cursor.fetchall()
        columnName = ("id", "collegeName", "collegeAddress", "collegeState", "collegeCity", "collegePhoneNumber")
        res = {
            "data": []
        }
        count = 0
        for x in resultt:
            res["data"].append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res
 