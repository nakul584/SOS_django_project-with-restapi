


from django.http import HttpResponse
from .BaseCtl import BaseCtl
from django.shortcuts import render,redirect
from service.utility.DataValidator import DataValidator
from service.service.UserService import UserService

class LogoutCtl(BaseCtl):

    def request_to_form(self,requestFrom):
        self.form["loginId"]  = requestFrom["loginId"]
        self.form["password"] = requestFrom["password"] 

    def input_validation(self):
        super().input_validation()
        inputError =  self.form["inputError"]
        if(DataValidator.isNull(self.form["loginId"])):
            inputError["loginId"] = "Login can not be null"
            self.form["error"] = True
        if(DataValidator.isNull(self.form["password"])):
            inputError["password"] = "Password can not be null"
            self.form["error"] = True

        return self.form["error"]

    def display(self,request,params={}):
        request.session["user"]=None
        self.form["message"]="Logout Successful"
        res = render(request,self.get_template(),{"form":self.form})
        return res

    def submit(self,request,params={}):
        pass
       

    # Template html of Role page    
    def get_template(self):
        return "Login.html"        

    # Service of Role     
    def get_service(self):
        return UserService()        