from django.shortcuts import render,HttpResponseRedirect
from.forms import StudentRegistration
from django.views.generic.base import TemplateView,RedirectView
from.models import user
from django.contrib import messages, auth
from django.views import View
from userproject import settings
# Create your views here.


class UserAddShow(TemplateView):
    template_name='enroll/addshow.html'
    def get_context_data(self,*args,**kwargs):
        contex=super().get_context_data(**kwargs)
        fm=StudentRegistration()
        stud=user.objects.all()
        contex={'stu':stud,'form':fm}
        return contex

    def post(self,request):
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm= fm.cleaned_data['name']
            em= fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg=user(name=nm,email=em,password=pw)
            reg.save()
        return HttpResponseRedirect('/') 

class UserDeleteView(RedirectView):
    url='/'
    def get_redirect_url(self,*args,**kwrgs):
        del_id=kwrgs['id']
        user.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args,**kwrgs)   

                                       
class UserUpdateView(View):
    def get(self,request,id):
        pi=user.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
        return render(request,'enroll/update.html',{'form':fm})

    def post(self,request,id):
        pi=user.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid:
            fm.save()   

        return HttpResponseRedirect('/')    



        

