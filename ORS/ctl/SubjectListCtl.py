

from django.http import HttpResponse
from .BaseCtl import BaseCtl
from django.shortcuts import render,redirect
from ORS.utility.DataValidator import DataValidator
from service.forms import SubjectForm
from service.models import Subject
from service.service.SubjectService import SubjectService  

class SubjectListCtl(BaseCtl):
    count=1

    def request_to_form(self,requestForm):
        self.form["subjectName"]=requestForm.get("subjectName",None)
        self.form["subjectDescription"]=requestForm.get("subjectDescription",None)
        self.form["course_ID"]=requestForm.get("course_ID",None)
        self.form["courseName"]=requestForm.get("courseName",None)
        self.form["ids"]= requestForm.getlist( "ids", None)

        

    def display(self,request,params={}):
        record = self.get_service().search(self.form)
        self.page_list=record["data"]
        res = render(request,self.get_template(),{"pageList":self.page_list})
        return res

    def next(self, request, params={}):    
        SubjectListCtl.count+=1
        self.form["pageNo"]=SubjectListCtl.count
        record = self.get_service().search(self.form)
        self.page_list=record["data"]
        res = render(request, self.get_template(), {"pageList": self.page_list,"form":self.form})
        return res
   
    def previous(self, request, params={}):    
        SubjectListCtl.count-=1
        self.form["pageNo"]=SubjectListCtl.count
        record = self.get_service().search(self.form)
        self.page_list=record["data"]
        res = render(request, self.get_template(), {"pageList": self.page_list,"form":self.form})
        return res


    def submit(self,request,params={}):
        self.request_to_form(request.POST)
        record = self.get_service().search(self.form)
        self.page_list=record["data"]
        res = render(request, self.get_template(), {"pageList": self.page_list, "form": self.form})
        return res
        
    def get_template(self):
        return "SubjectList.html"          

    # Service of Marksheet     
    def get_service(self):
        return SubjectService()        

    def deleteRecord(self,request,params={}):
        SubjectListCtl.count+=1
        self.form["pageNo"]=1
        if(bool(self.form["ids"])==False):
            self.form["error"] = True
            self.form["message"] = "Please Select at least one check box"
            return render(request,self.get_template(),{"pageList":self.page_list,"form":self.form})
        else:
            for ids in self.form["ids"]:
                record = self.get_service().search(self.form)
                self.page_list=record["data"]

                id=int(ids)
                if( id > 0):
                    r = self.get_service().get(id)
                    if r is not None:
                        self.get_service().delete(r.id)
                        record = self.get_service().search(self.form)
                        self.page_list=record["data"]
                        self.form["pageNo"]=1

                        self.form["error"] = False
                        self.form["message"] = "DATA IS SUCCESSFULLY DELETED"
                        print("ppppppp-->",self.page_list)
                        return render(request,self.get_template(),{"pageList":self.page_list,"form":self.form})
                    else:
                        self.form["error"] = True
                        self.form["message"] = "Data is not deleted"
                        return render(request,self.get_template(),{"pageList":self.page_list,"form":self.form})
