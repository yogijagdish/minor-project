from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    return render(request,'pages/home.html',
    {'link1':'http://127.0.0.1:8000/',
    'link2':'http://127.0.0.1:8000/frontend/trek',
    'link3':'http://127.0.0.1:8000/frontend/guide',
    'link4':'http://127.0.0.1:8000/frontend/curentrecord',
    'link5':'http://127.0.0.1:8000/frontend/contactus'})

def trek(request):
    return render(request,'pages/trek/trek.html',
    {'link1':'http://127.0.0.1:8000/',
    'link2':'http://127.0.0.1:8000/frontend/trek',
    'link3':'http://127.0.0.1:8000/frontend/guide',
    'link4':'http://127.0.0.1:8000/curentrecord',
    'link5':'http://127.0.0.1:8000/frontend/contactus',
    'link6':'http://127.0.0.1:8000/frontend/trek/mardi',
    'link7':'http://127.0.0.1:8000/frontend/trek/tilicho',
    'link8':'http://127.0.0.1:8000/frontend/trek/langtang'})

def langtang(request):
    return render(request,'pages/trek/langtang.html',
    {'link1':'http://127.0.0.1:8000/',
    'link2':'http://127.0.0.1:8000/frontend/trek',
    'link3':'http://127.0.0.1:8000/frontend/guide',
    'link4':'http://127.0.0.1:8000/frontend/curentrecord',
    'link5':'http://127.0.0.1:8000/frontend/contactus'})

def mardi(request):
    return render(request,'pages/trek/mardi.html',
    {'link1':'http://127.0.0.1:8000/',
    'link2':'http://127.0.0.1:8000/frontend/trek',
    'link3':'http://127.0.0.1:8000/frontend/guide',
    'link4':'http://127.0.0.1:8000/frontend/curentrecord',
    'link5':'http://127.0.0.1:8000/frontend/contactus'})

def tilicho(request):
    return render(request,'pages/tilicho.html',
    {'link1':'http://127.0.0.1:8000/',
    'link2':'http://127.0.0.1:8000/frontend/trek',
    'link3':'http://127.0.0.1:8000/frontend/guide',
    'link4':'http://127.0.0.1:8000/frontend/curentrecord',
    'link5':'http://127.0.0.1:8000/frontend/contactus'})

def guide(request):
    return render(request,'pages/guide.html',
    {'link1':'http://127.0.0.1:8000/',
    'link2':'http://127.0.0.1:8000/frontend/trek',
    'link3':'http://127.0.0.1:8000/frontend/guide',
    'link4':'http://127.0.0.1:8000/frontend/curentrecord',
    'link5':'http://127.0.0.1:8000/frontend/contactus'})

def contact_us(request):
    return render(request,'pages/contactus.html',
    {'link1':'http://127.0.0.1:8000/',
    'link2':'http://127.0.0.1:8000/frontend/trek',
    'link3':'http://127.0.0.1:8000/frontend/guide',
    'link4':'http://127.0.0.1:8000/frontend/curentrecord',
    'link5':'http://127.0.0.1:8000/frontend/contactus'})

def curent_record(request):
    return render(request,'pages/curentrecord.html',
    {'link1':'http://127.0.0.1:8000/',
    'link2':'http://127.0.0.1:8000/frontend/trek',
    'link3':'http://127.0.0.1:8000/frontend/guide',
    'link4':'http://127.0.0.1:8000/frontend/curentrecord',
    'link5':'http://127.0.0.1:8000/frontend/contactus'})

