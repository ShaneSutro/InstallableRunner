import sys
import os
import queueWorker

sys.path.append(os.getcwd() + "/installables")
import repository  # noqa: E402

q = queueWorker.queue


def queue(queueTime, installable, jobID):
    # NOTE: Installable should be a dict with the name and URL
    result = q.enqueue_at(queueTime, repository.run(installable), jobID)
    print(result)
