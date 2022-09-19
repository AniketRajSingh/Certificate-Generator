# This file is created by Aniket Raj Singh
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def certificates(request):
    certback1='https://raw.githubusercontent.com/AniketRajSingh/Certificate-Generator/aniket_master/static/admin/img/Certificate_template_1.png'
    certback2='https://raw.githubusercontent.com/AniketRajSingh/Certificate-Generator/aniket_master/static/admin/img/Certificate_template_2.png'
    certback3='https://raw.githubusercontent.com/AniketRajSingh/Certificate-Generator/aniket_master/static/admin/img/Certificate_template_3.png'
    param={'name':'Aniket','middlename':'Raj','sirname':'Singh','language':'Django','cert_background':certback1,'certback1':certback1,'certback2':certback2,'certback3':certback3,'gender':'his/her','gender1':'him/her','gender2':'Mr/Miss'}
    firstn=request.POST.get('fname','Aniket')
    middlen=request.POST.get('mname','Raj')
    lastn=request.POST.get('lname','Singh')
    langn=request.POST.get('lang','Django')
    gender=request.POST.get('gender','his/her')
    gender1=gender
    gender2='Mr/Miss'
    certbackground=request.POST.get('certbackground','default')
    if firstn == '' or langn=='' or certbackground=='default' or gender=='his/her':
        defaultans='One or Multiple important blanks that includes First name, Language and background selection has been left blank, thus the system is generating default output with default selections. '
        certbackground=certback1
    else:
        defaultans=''

    if gender == 'male' :
        gender='his'
        gender1='him'
        gender2='Mr'
    elif gender =='female':
        gender='her'
        gender1='her'
        gender2='Miss'

    certbackground=request.POST.get('certbackground',certback1)
    param.update({'name':firstn,'middlename':middlen,'sirname':lastn,'language':langn,'cert_background':certbackground,'defaultans':defaultans,'gender':gender,'gender1':gender1,'gender2':gender2})
    return render(request,'certificates.html',param)
def certform(request):
    certback1='https://raw.githubusercontent.com/AniketRajSingh/Certificate-Generator/aniket_master/static/admin/img/Certificate_template_1.png'
    certback2='https://raw.githubusercontent.com/AniketRajSingh/Certificate-Generator/aniket_master/static/admin/img/Certificate_template_2.png'
    certback3='https://raw.githubusercontent.com/AniketRajSingh/Certificate-Generator/aniket_master/static/admin/img/Certificate_template_3.png'
    param1={'certback1':certback1,'certback2':certback2,'certback3':certback3}
    return render(request,'cert_gen_form.html',param1)