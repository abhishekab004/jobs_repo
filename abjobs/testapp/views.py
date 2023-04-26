from django.shortcuts import render
from testapp.models import HydJobs,BangaloreJobs,PuneJobs

# Create your views here.

def homepage_view(request):
    return render(request,'testapp/index.html')

def hydjobs_view(request):
    jobs_list = HydJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render (request,'testapp/hydjobs.html',context=my_dict)

def bangalore_view(request):
    jobs_list = BangaloreJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render (request,'testapp/bang.html',context=my_dict)

def pune_view(request):
    jobs_list = PuneJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render (request,'testapp/pune.html',context=my_dict)
