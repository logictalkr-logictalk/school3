from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from .models import Emp
from django.views.generic import View

class home(View):
    def get(self,request):
        return render(request,'reg.html')

class emp(View):
    def post(self,request):
        try:
            sname = (request.POST['sname'])
            regno = (request.POST['regno'])
            board = (request.POST['board'])
            location = (request.POST['location'])
            city = (request.POST['city'])
            pin = (request.POST['pin'])
            state = (request.POST['state'])
            email = (request.POST['email'])
            mob = (request.POST['mob'])
            mobile = (request.POST['mobile'])
            land = (request.POST['land'])
            landline = (request.POST['landline'])
            pwd = (request.POST['pwd'])
            psw = (request.POST['psw'])

            reg = Emp(Name_of_the_school=sname,
                      Regno=regno,
                      Board=board,
                      Location=location,
                      City=city,
                      Pin=pin,
                      State=state,
                      School_email=email,
                      Mobile_no=mob,
                      Mobile_no1=mobile,
                      Land_line=land,
                      Land_line1=landline,
                      Password=pwd,
                      Con_password=psw)
            reg.save()
            return HttpResponse('<h1>Registration Successful</h1>')
        except:
            return render(request, 'login.htm')


class Reg(View):
    def get(self,request):
        return render(request,'login.html')





