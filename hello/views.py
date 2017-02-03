from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient
from .models import Greeting

import requests

def index(request):
    client = MongoClient('mongodb://back:1234@ds035059.mlab.com:35059/heroku_mqq5pbhp')
    db = client['heroku_mqq5pbhp']
    collection = db['airquality']
    results = collection.find()

    for record in results:
        print(record['raw'])

    return HttpResponse('<pre>' + print results[0]['raw'] + '</pre>')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

