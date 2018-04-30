from django.conf import settings
from django.utils import translation
from .models import *
from django.contrib.auth.models import Group
from django.utils.deprecation import MiddlewareMixin


class ForceLangMiddleware:
    def process_request(self, request):
        request.LANG = getattr(settings, 'LANGUAGE_CODE', settings.LANGUAGE_CODE)
        translation.activate(request.LANG)
        request.LANGUAGE_CODE = request.LANG
        if request.user.is_authenticated():
            # if not request.session['EmpID']:
            email = request.user.email
            emp = Employee.objects.filter(email= email)
            # Get all data filtered by user email and set in session
            for data in emp:
                request.session['EmpID'] = data.empid
                request.session['EmpName'] = data.empname
                request.session['DeptName'] = data.deptname
                request.session['Mobile'] = data.mobile
                request.session['JobTitle'] = data.jobtitle
                request.session['DeptCode'] = data.deptcode
                if data.ismanager == 1:
                    g = Group.objects.get(name='ismanager')
                    g.user_set.add(request.user.id)
                    request.session['IsManager'] = True
                else:
                    g = Group.objects.get(name='employee')
                    g.user_set.add(request.user.id)
                obj_emp = Delegation.objects.filter(authorized = data.empid , expired="0")
                if obj_emp:
                    request.session['have_auth']  = True
                    
class UserSeesionSet:
    def UserSessions(request):
        if request.user.is_authenticated():
            email = request.user.email
            emp = Employee.objects.filter(email= email)
            # Get all data filtered by user email and set in session
            for data in emp:
                request.session['EmpID'] = data.empid
                request.session['EmpName'] = data.empname
                request.session['DeptName'] = data.deptname
                request.session['Mobile'] = data.mobile
                request.session['DeptCode'] = data.deptcode
