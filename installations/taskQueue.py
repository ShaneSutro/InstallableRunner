import sys
import os
import queueWorker

sys.path.append(os.getcwd() + "/installables")
import repository  # noqa: E402

q = queueWorker.queue


def queue(queueTime, installable, jobID):
    # NOTE: Installable should be a dict with the name and URL
    def partial(f, *args):
        def wrapped(*args2):
            return f(*args, *args2)
        return wrapped
    perform = partial(repository.run, installable)

    result = q.enqueue_at(queueTime, perform, job_id=jobID)
    print(result)
    print(result.id)

