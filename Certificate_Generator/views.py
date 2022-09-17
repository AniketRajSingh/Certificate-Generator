# This file is created by Aniket Raj Singh
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def certificates(request):
    param={'name':'Aniket','middlename':'Raj','sirname':'Singh','language':'Django'}
    firstn=request.GET.get('fname','Aniket')
    middlen=request.GET.get('mname','Raj')
    lastn=request.GET.get('lname','Singh')
    langn=request.GET.get('lang','Django')
    param.update({'name':firstn,'middlename':middlen,'sirname':lastn,'language':langn})
    print(firstn)
    return render(request,'certificates.html',param)
def certform(request):
    return render(request,'cert_gen_form.html')