import os
import sys
import timefrequencies as tf
from taskQueue import queue
import datetime

sys.path.append(os.getcwd() + "/database")
from db import client as db  # noqa: E402


def scheduleAll():
    now = datetime.datetime.now()
    timeRangeStart = now + datetime.timedelta(hours=1)
    timeRangeEnd = now + datetime.timedelta(hours=2)
    allInstallations = db.installations.find({})
    for inst in allInstallations:
        repo = db.installables.find_one({"name": inst["installable"]})
        installation = {"name": inst["installable"], "url": repo["url"]}
        # Function call returns an list of dicts where each one has a
        # {'time': datetime object and a 'job': job ID string}
        # If none fall within the time it is already scheduled,
        # it will be skipped.
        jobs = schedulers[inst["frequency"]](inst, timeRangeStart, timeRangeEnd, now)
        if jobs:
            print("Scheduling", len(jobs), "job(s)")
            for job in jobs:
                queue(job['time'], installation, job['job'])


schedulers = {
    "minutely": tf.minutely,
    "hourly": tf.hourly,
    "daily": tf.daily,
    "weekly": tf.weekly,
    "monthly": tf.monthly,
}

if __name__ == "__main__":
    scheduleAll()
