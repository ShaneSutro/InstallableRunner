def minutely(installation, timeRangeStart, timeRangeEnd):
    print("Minutely")
    allJobs = {}
    # NOTE: Only allow 1, 5, 10, 20, 30 increments
    subID = installation['subID']
    every_x_minutes = installation['startingAt']['every_x_minutes']
    on_the = installation['startingAt']['on_the']
    
    # TODO: Check if exists in queue
    # TODO: If so, skip
    # TODO: If not, add each minute for the next hour
    pass


def hourly(installation, timeRangeStart, timeRangeEnd):
    print("Hourly")
    # TODO: Check if exists in queue
    # TODO: If so, skip
    # TODO: If not, get minute from DB
    # TODO: Check if minute/hour match up with the next time period
    # TODO: If so, schedule
    # TODO: If not, skip
    pass


def daily(installation, timeRangeStart, timeRangeEnd):
    print("Daily")
    # TODO: Check if exists in queue and skip if so
    # TODO: Get hour/minute from db
    # TODO: If hour/minute combo match up, schedule
    # TODO: Else skip
    pass


def weekly(installation, timeRangeStart, timeRangeEnd):
    print("Weekly")
    pass


def monthly(installation, timeRangeStart, timeRangeEnd):
    print("Monthly")
    pass
