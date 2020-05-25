from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
import mysql.connector
import requests

httpAPI = 'https://wl8kv6aold.execute-api.us-east-1.amazonaws.com/default/lambda-test'

# DB connection
def db_connection():
    mydb = mysql.connector.connect(
    host = 'database-2.cso3cavr2hlm.us-east-1.rds.amazonaws.com', 
	user = 'admin',
    port = '3306', 
	database = 'ncov',
    passwd = 'Welcome1'
    )
    return mydb

def non_return_db_operation(request):
    mydb = db_connection()
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute(request)
    mydb.commit()

def publishhandler(request):
    ID = request.POST["S_ID"]
    location = request.POST['S_LOCATION']
    name = request.POST['S_NAME']
    email = request.POST['S_EMAIL']
    from_country = request.POST['S_From_country']
    temp = request.POST['S_Body_temp']
    hstatus = request.POST['S_Health_status']
    request = "insert into record values(null, '" + ID + "', '" + name + "','" + email + "', '" + location + "', '" + from_country  + "', '" + temp  + "', '" + hstatus + "')"
    non_return_db_operation(request)
    #invoke = requests.get(httpAPI)
    return HttpResponseRedirect('/records')

def all_return_db_operation(request):
    mydb = db_connection()
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute(request)
    records = mycursor.fetchall()
    return records

def records(request):
    trecords = all_return_db_operation('select * from record')
    records = []
    for tr in trecords:
        records.append({"recordID": tr[0],
           "ID": tr[1],
           "name": tr[2],
           "email": tr[3],
           "Location":tr[4],
           "FromCountry" : tr[5],
           "BodyTemp": tr[6],
           "HealthStatus" : tr[7],
    })
    context = {'records':records}
    return render(request, 'COMP4442_project/records.html', context)


def index(request):
    return HttpResponse("Hello World")

def form(request):
    context ={}
    return render(request, 'COMP4442_project/form.html', context)