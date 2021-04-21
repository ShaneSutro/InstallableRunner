from queueWorker import queue
import datetime


def minutely(installation, timeRangeStart, timeRangeEnd, now):
    print("Minutely")
    allJobs = {}
    # NOTE: Only allow 1, 5, 10, 20, 30 increments
    subID = installation['subID']
    every_x_minutes = installation['startingAt']['every_x_minutes']
    on_the = installation['startingAt']['on_the']
    timeframe = timeRangeEnd - timeRangeStart
    print((timeframe.seconds / every_x_minutes) / 60)
    print((timeRangeEnd - timeRangeStart) / every_x_minutes)
    return False  # Temp
    # TODO: Check if exists in queue
    # TODO: If so, skip
    # TODO: If not, add each minute for the next hour


def hourly(installation, timeRangeStart, timeRangeEnd, now):
    subID = installation['subID']
    scheduleTime = datetime.datetime(
        timeRangeStart.year,
        timeRangeStart.month,
        timeRangeStart.day,
        timeRangeStart.hour,
        installation['startingAt']['minute']
    )
    scheduleString = datetime.datetime.strftime(scheduleTime, "%H:%M")
    jobID = f'{subID} {scheduleString}'

    if jobID in queue.scheduled_job_registry:
        print('This job is already scheduled.')
        return False
    else:
        return [{"time": scheduleTime, "job": jobID}]


def daily(installation, timeRangeStart, timeRangeEnd, now):
    print("Daily")
    # TODO: Check if exists in queue and skip if so
    # TODO: Get hour/minute from db
    # TODO: If hour/minute combo match up, schedule
    # TODO: Else skip
    return False


def weekly(installation, timeRangeStart, timeRangeEnd, now):
    print("Weekly")
    return False


def monthly(installation, timeRangeStart, timeRangeEnd, now):
    print("Monthly")
    return False
