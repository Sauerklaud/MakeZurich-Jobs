from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient
from .models import Greeting
import requests
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    print('This job is run every three minutes.')

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

sched.start()


def index(request):
    client = MongoClient('mongodb://back:1234@ds035059.mlab.com:35059/heroku_mqq5pbhp')
    db = client['heroku_mqq5pbhp']
    collection = db['airquality']
    results = collection.find()

    noOfRecords = 0
    for record in results:
        noOfRecords = noOfRecords + 1
        print(record['raw'])
    print(noOfRecords)
    return HttpResponse('<pre>' + str(noOfRecords) + '</pre>')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

