# Collection of functions that interact with a list of tasks
import Task
import IOFunctions


# adds one task to the list
# TODO insert task in chronological order
def add_task(task_list, task):
    task_list.append(task)
    return task_list
