

from django.http import HttpResponse
from .BaseCtl import BaseCtl
from django.shortcuts import render
from ORS.utility.DataValidator import DataValidator
from service.models import Marksheet
from service.forms import MarksheetForm
from service.service.MarksheetService import MarksheetService
from service.service.StudentService import StudentService

class MarksheetMeritListCtl(BaseCtl):
    
    #Display Marksheet page 
    def display(self,request,params={}):
        res = render(request,self.get_template())
        return res

    #Submit Marksheet page
    def submit(self,request,params={}):
        res = render(request,self.get_template())
        return res
        
    # Template html of Role page    
    def get_template(self):
        return "MarksheetMeritList.html"          

    # Service of Role     
    def get_service(self):
        return MarksheetService()        
