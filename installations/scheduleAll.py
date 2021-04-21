import os
import sys
import timefrequencies as tf
from taskQueue import queue
import datetime

sys.path.append(os.getcwd() + "/database")
from db import client as db  # noqa: E402


def scheduleAll():
    now = datetime.datetime.now()
    timeRangeStart = now + datetime.timedelta(hours=1) - datetime.timedelta(minutes=1)
    timeRangeEnd = now + datetime.timedelta(hours=2)
    allInstallations = db.installations.find({})
    for inst in allInstallations:
        repo = db.installables.find_one({"name": inst["installable"]})
        installation = {"name": inst["installable"], "url": repo["url"]}
        jobs = schedulers[inst["frequency"]](inst, timeRangeStart, timeRangeEnd)
        if jobs:
            for job in jobs:
              queue(scheduleTime, installation, "VBTEST 13:45")
        # XXX: Should return a date-time object for when this should be
        # XXX: scheduled or False if it should not be scheduled?


schedulers = {
    "minutely": tf.minutely,
    "hourly": tf.hourly,
    "daily": tf.daily,
    "weekly": tf.weekly,
    "monthly": tf.monthly,
}

if __name__ == "__main__":
    scheduleAll()
