from apscheduler.schedulers.blocking import BlockingScheduler
from pymongo import MongoClient
import pusher
import logging
logging.basicConfig()

sched = BlockingScheduler()

#@sched.scheduled_job('interval', minutes=1)
#def timed_job():
#    client = MongoClient('mongodb://back:1234@ds035059.mlab.com:35059/heroku_mqq5pbhp')
#    db = client['heroku_mqq5pbhp']
#    collection = db['airquality']
#    results = collection.find()

#    noOfRecords = 0
#    for record in results:
#       noOfRecords = noOfRecords + 1
#       print(record['raw'])
#   print('Number of db-entries: ' + str(noOfRecords))

#    client.close()


pusher_client = pusher.Pusher(
    app_id='298067', 
    key='256b563cc59616398c15', 
    secret='ad03aff71ebb5af9bacc', 
    cluster='eu', 
    ssl=True)

@sched.scheduled_job('interval', seconds=5)
def timed_job():
    pusher_client.trigger('my-channel', 'my-event', 
    {'message': {
        "pm10": '342',
        "pm25": '430',
        "latitude": '47.5',
        "longitude": '7.5',
        "timestamp": '2343242',
        "meas_id": '4342',
        "isValid": 'true'
    }})

sched.start()