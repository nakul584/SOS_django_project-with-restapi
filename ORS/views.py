from django.conf.urls.static import static
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from .ctl.UserCtl import UserCtl
from .ctl.CollegeCtl import CollegeCtl
from .ctl.LoginCtl import LoginCtl
from .ctl.WelcomeCtl import WelcomeCtl
from .ctl.RoleCtl import RoleCtl
from .ctl.RoleListCtl import RoleListCtl
from .ctl.AddFacultyCtl import AddFacultyCtl
from .ctl.AddFacultyListCtl import AddFacultyListCtl
from .ctl.CourseCtl import CourseCtl
from .ctl.StudentCtl import StudentCtl
from .ctl.MarksheetCtl import MarksheetCtl
from .ctl.MarksheetMeritListCtl import MarksheetMeritListCtl
from .ctl.SubjectCtl import SubjectCtl
from .ctl.SubjectListCtl import SubjectListCtl
from .ctl.TimeTableCtl import TimeTableCtl
from .ctl.TimeTableListCtl import TimeTableListCtl
from .ctl.UserListCtl import UserListCtl
from .ctl.UserCtl import UserCtl
from .ctl.CollegeListCtl import CollegeListCtl
from .ctl.CourseListCtl import CourseListCtl
from .ctl.MarksheetListCtl import MarksheetListCtl
from .ctl.StudentListCtl import StudentListCtl
from .ctl.RegistrationCtl import RegistrationCtl
from .ctl.ForgetPasswordCtl import ForgetPasswordCtl
from .ctl.ChangePasswordCtl import ChangePasswordCtl
from .ctl.LogoutCtl import LogoutCtl
from .ctl.MyProfileCtl import MyProfileCtl
from .ctl.HomeCtl import HomeCtl

@csrf_exempt
def action(request, page, action=""):
    ctlName = page + "Ctl()"
    ctlObj = eval(ctlName)
    return ctlObj.execute(request, {"id": 0})


'''
Calls respective controller with id
'''

@csrf_exempt
def actionId(request, page="", operation="", id=0):
    if request.session.get('user') is not None and page != "":
        ctlName = page + "Ctl()"
        ctlObj = eval(ctlName)
        res = ctlObj.execute(request, {"id": id})
    elif page == "Registration":
        ctlName = "Registration" + "Ctl()"
        ctlObj = eval(ctlName)
        res = ctlObj.execute(request, {"id": id})
    elif page == "Home":
        ctlName = "Home" + "Ctl()"
        ctlObj = eval(ctlName)
        res = ctlObj.execute(request, {"id": id})

    elif page == "ForgetPassword":
        ctlName = "ForgetPassword" + "Ctl()"
        ctlObj = eval(ctlName)
        res = ctlObj.execute(request, {"id": id})

    else:
        ctlName = "Login" + "Ctl()"
        ctlObj = eval(ctlName)
        res = ctlObj.execute(request, {"id": id})
    return res


@csrf_exempt
def auth(request, page="", operation="", id=0):
    if page == "Logout":
        Session.objects.all().delete()
        ctlName = page + "Ctl()"
        ctlObj = eval(ctlName)
        res = ctlObj.execute(request, {"id": id, "operation": operation})

    elif page == "ForgetPassword":
        ctlName = "ForgetPassword" + "Ctl()"
        ctlObj = eval(ctlName)
        res = ctlObj.execute(request, {"id": id, "operation": operation})

    else:
        ctlName = "Login" + "Ctl()"
        ctlObj = eval(ctlName)
        res = ctlObj.execute(request, {"id": id, "operation": operation})
    return res


def index(request):
    res = render(request, 'project.html')
    return res
