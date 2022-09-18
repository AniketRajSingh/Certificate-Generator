# This file is created by Aniket Raj Singh
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def certificates(request):
    certback1='https://raw.githubusercontent.com/AniketRajSingh/Certificate-Generator/aniket_master/static/admin/img/Certificate_template_1.png'
    certback2='https://raw.githubusercontent.com/AniketRajSingh/Certificate-Generator/aniket_master/static/admin/img/Certificate_template_2.png'
    param={'name':'Aniket','middlename':'Raj','sirname':'Singh','language':'Django','cert_background':certback1,'certback1':certback1,'certback2':certback2}
    firstn=request.GET.get('fname','Aniket')
    middlen=request.GET.get('mname','Raj')
    lastn=request.GET.get('lname','Singh')
    langn=request.GET.get('lang','Django')
    certbackground=request.GET.get('certbackground','default')
    if firstn == '' or langn=='' or certbackground=='default' :
        defaultans='One or Multiple important blanks that includes First name, Language and background selection has been left blank, thus the system is generating default output with default selections. '
        certbackground=certback1
    else:
        defaultans=''


    certbackground=request.GET.get('certbackground',certback1)
    param.update({'name':firstn,'middlename':middlen,'sirname':lastn,'language':langn,'cert_background':certbackground,'defaultans':defaultans})
    return render(request,'certificates.html',param)
def certform(request):
    certback1='https://raw.githubusercontent.com/AniketRajSingh/Certificate-Generator/aniket_master/static/admin/img/Certificate_template_1.png'
    certback2='https://raw.githubusercontent.com/AniketRajSingh/Certificate-Generator/aniket_master/static/admin/img/Certificate_template_2.png'
    param1={'certback1':certback1,'certback2':certback2}
    return render(request,'cert_gen_form.html',param1)