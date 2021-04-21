import os, sys
import timefrequencies as tf

sys.path.append(os.getcwd() + '/database')
from db import client as db

def scheduleAll():
  allInstallations = db.installations.find({})
  for inst in allInstallations:
    repo = db.installables.find_one({'name': inst['installable']})['name']
    # frequency = inst['frequency']
    schedulers[inst['frequency']](inst)

schedulers = {
  'minutely': tf.minutely,
  'hourly': tf.hourly,
  'daily': tf.daily,
  'weekly': tf.weekly,
  'monthly': tf.monthly
}

if __name__ == "__main__":
  scheduleAll()