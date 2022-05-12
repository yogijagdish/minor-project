from dataclasses import field
from dis import dis
from django.shortcuts import render
from . models import climate, climate_langtang, climate_tilicho,sensor_data
import mysql.connector
import requests

# Calling api to fetch data from databases.
def api_mardi():
    try:
        mydb = mysql.connector.connect(host="localhost",user="jagdish",passwd="Jagdish@1234",database="final_project")
        mycursor = mydb.cursor()
        response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=mardi&appid=b44fcb0e2f09d3ef62d74f75f15c4820").json()

        dist = response['weather']
        dist1 = response['main']
        dist2 = dist[0]
        main = dist2.get('main')
        description = dist2.get('description')
        temp = dist1.get('temp')
        temp_min = dist1.get('temp_min')
        temp_max = dist1.get('temp_max')
        lst = [main,description,temp,temp_min,temp_max]
        
        query1 = "insert into frontend_climate values(%s,%s,%s,%s,%s)"
        mycursor.execute(query1,lst)
        mydb.commit()
    except:
        pass

def api_tilicho():
    try:
        mydb = mysql.connector.connect(host="localhost",user="jagdish",passwd="Jagdish@1234",database="final_project")
        mycursor = mydb.cursor()
        response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=manang&appid=b44fcb0e2f09d3ef62d74f75f15c4820").json()

        dist = response['weather']
        dist1 = response['main']
        dist2 = dist[0]
        main = dist2.get('main')
        description = dist2.get('description')
        temp = dist1.get('temp')
        temp_min = dist1.get('temp_min')
        temp_max = dist1.get('temp_max')
        lst = [main,description,temp,temp_min,temp_max]
        
        query1 = "insert into frontend_climate_tilicho values(%s,%s,%s,%s,%s)"
        mycursor.execute(query1,lst)
        mydb.commit()
    except:
        pass
    
def api_langtang():
    try:
        mydb = mysql.connector.connect(host="localhost",user="jagdish",passwd="Jagdish@1234",database="final_project")
        mycursor = mydb.cursor()
        response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=langtang&appid=b44fcb0e2f09d3ef62d74f75f15c4820").json()

        dist = response['weather']
        dist1 = response['main']
        dist2 = dist[0]
        main = dist2.get('main')
        description = dist2.get('description')
        temp = dist1.get('temp')
        temp_min = dist1.get('temp_min')
        temp_max = dist1.get('temp_max')
        lst = [main,description,temp,temp_min,temp_max]
        
        query1 = "insert into frontend_climate_langtang values(%s,%s,%s,%s,%s)"
        mycursor.execute(query1,lst)
        mydb.commit()
    except:
        pass

def api_tempreture():
    try:
        mydb = mysql.connector.connect(host="localhost",user="jagdish",passwd="Jagdish@1234",database="final_project")
        mycursor = mydb.cursor()
        response = requests.get("https://api.thingspeak.com/channels/1722499/feeds.json?api_key=7QXFCH4NWJHK649Y&results=5").json()

        dist = response['feeds']
        for i in range(5):
            dist1 = dist[i]
            created_at = dist1.get("created_at")
            entry = dist1.get('entry_id')
            field1 = dist1.get("field1")
            field2 = dist1.get("field2")
            dist1 = [created_at,entry,field1,field2]
            query1 = "insert into frontend_sensor_data values(%s,%s,%s,%s)"
            mycursor.execute(query1,dist1)
            mydb.commit()
    except:
        pass

# Rendering the webpages


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
    api_langtang()
    climate_langtang1 = climate_langtang.objects.all()
    return render(request,'pages/trek/langtang.html',
    {'link1':'http://127.0.0.1:8000/',
    'link2':'http://127.0.0.1:8000/frontend/trek',
    'link3':'http://127.0.0.1:8000/frontend/guide',
    'link4':'http://127.0.0.1:8000/frontend/curentrecord',
    'link5':'http://127.0.0.1:8000/frontend/contactus',
    'climate_langtang2':climate_langtang1})

def mardi(request):
    api_mardi()
    climate1 = climate.objects.all().reverse()
    return render(request,'pages/trek/mardi.html',
    {'link1':'http://127.0.0.1:8000/',
    'link2':'http://127.0.0.1:8000/frontend/trek',
    'link3':'http://127.0.0.1:8000/frontend/guide',
    'link4':'http://127.0.0.1:8000/frontend/curentrecord',
    'link5':'http://127.0.0.1:8000/frontend/contactus',
    'climate2':climate1})

def tilicho(request):
    api_tilicho()
    climate_tilicho1 = climate_tilicho.objects.all().reverse()
    return render(request,'pages/trek/tilicho.html',
    {'link1':'http://127.0.0.1:8000/',
    'link2':'http://127.0.0.1:8000/frontend/trek',
   'link3':'htp://127.0.0.1:8000/frontend/guide',
    'link4':'http://127.0.0.1:8000/frontend/curentrecord',
    'link5':'http://127.0.0.1:8000/frontend/contactus',
    'climate_tilicho2':climate_tilicho1})

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

def trekker1(request):
    api_tempreture()
    sensor_tempreture1 = sensor_data.objects.all()
    return render(request,'pages/current/trekker1.html',
    {'link1':'http://127.0.0.1:8000/',
    'link2':'http://127.0.0.1:8000/frontend/trek',
    'link3':'http://127.0.0.1:8000/frontend/guide',
    'link4':'http://127.0.0.1:8000/frontend/curentrecord',
    'link5':'http://127.0.0.1:8000/frontend/contactus',
    'link6' : '192.168.1.71',
    'sensor_tempreture2':sensor_tempreture1})

def curent_record(request):
    return render(request,'pages/curentrecord.html', 
    {'link1':'http://127.0.0.1:8000/',
    'link2':'http://127.0.0.1:8000/frontend/trek',
    'link3':'http://127.0.0.1:8000/frontend/guide',
    'link4':'http://127.0.0.1:8000/frontend/curentrecord',
    'link5':'http://127.0.0.1:8000/frontend/contactus',
    'link6':'http://127.0.0.1:8000/frontend/current/trekker1'})

