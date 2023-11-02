# Maintains lists that hold task name and date

def create_task(name, date):
    return [name, date]


def change_task_name(List, name):
    return [name, List(1)]


def change_task_date(List, date):
    return [List(0), date]
