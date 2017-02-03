from apscheduler.schedulers.blocking import BlockingScheduler
from pymongo import MongoClient

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    client = MongoClient('mongodb://back:1234@ds035059.mlab.com:35059/heroku_mqq5pbhp')
    db = client['heroku_mqq5pbhp']
    collection = db['airquality']
    results = collection.find()

    noOfRecords = 0
    for record in results:
        noOfRecords = noOfRecords + 1
        print(record['raw'])
    print('Number of db-entries: ' + str(noOfRecords))

    client.close()
    
sched.start()