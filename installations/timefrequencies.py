from queueWorker import queue
import datetime


def createScheduleTime(year, month, day, hour, minute, subID):
    """
    Returns a datetime object and a string version
    of the jobID
    """
    scheduleTime = datetime.datetime(
        year,
        month,
        day,
        hour,
        minute
    )
    skedString = datetime.datetime.strftime(scheduleTime, "%H:%M")
    jobID = f'{subID} {skedString}'
    return scheduleTime, jobID


def isAlreadyScheduled(registry, jobID):
    """
    Checks if current job is already listed in the queue registry
    """
    if jobID in registry:
        return True
    else:
        return False


def minutely(installation, timeRangeStart, timeRangeEnd, now, registry):
    print("Minutely")
    allJobs = {}
    # NOTE: Only allow 1, 5, 10, 20, 30 increments
    subID = installation["subID"]
    every_x_minutes = installation["startingAt"]["every_x_minutes"]
    on_the = installation["startingAt"]["on_the"]
    timeframe = timeRangeEnd - timeRangeStart
    print((timeframe.seconds / every_x_minutes) / 60)
    print((timeRangeEnd - timeRangeStart) / every_x_minutes)
    return False  # Temp
    # TODO: Check if exists in queue
    # TODO: If so, skip
    # TODO: If not, add each minute for the next hour


def hourly(installation, timeRangeStart, timeRangeEnd, now, registry):
    """
    Hourly calls are always scheduled, no need to check the current
    time. Since the scheduler will be run hourly, items that are to be
    scheduled hourly will be scheduled for the next hour on each run.
    """
    subID = installation["subID"]
    scheduleTime, jobID = createScheduleTime(
        timeRangeStart.year,
        timeRangeStart.month,
        timeRangeStart.day,
        timeRangeStart.hour,
        installation['startingAt']['minute'],
        installation['subID']
    )

    if isAlreadyScheduled(registry, jobID):
        print('This job is already scheduled.')
        return False
    else:
        return [{"time": scheduleTime, "job": jobID}]


def daily(installation, timeRangeStart, timeRangeEnd, now, registry):
    print("Daily")
    subID = installation["subID"]
    skedHour = installation["startingAt"]["hour"]
    skedMinute = installation["startingAt"]["minute"]
    if skedHour == timeRangeStart.hour:
        scheduleTime, jobID = createScheduleTime(
            timeRangeStart.year,
            timeRangeStart.month,
            timeRangeStart.day,
            skedHour,
            skedMinute,
            installation['subID']
        )
    # TODO: Check if exists in queue and skip if so
    # TODO: Get hour/minute from db
    # TODO: If hour/minute combo match up, schedule
    # TODO: Else skip
    return False


def weekly(installation, timeRangeStart, timeRangeEnd, now, registry):
    print("Weekly")
    return False


def monthly(installation, timeRangeStart, timeRangeEnd, now, registry):
    print("Monthly")
    return False
