# Collection of IO functions for ToDoList app
# Deals with To Do List as a csv file
import csv


# writes one task to file
def write_list(task_list):
    with open('ToDoList.csv',
              'w', newline='') as csvfile:
        list_file = csv.writer(csvfile)
        for row in task_list:
            list_file.writerow(row)


# returns list file as list of tasks
def read_list():
    list_file = []
    with open('ToDoList.csv',
              'r', newline='') as csvfile:
        list_file = list(csv.reader(csvfile))
    return list_file


# prints contents of task list
def print_task_list(task_list):
    for row in task_list:
        print(', '.join(row))


# gets task from the user and returns name as a string
# TODO check input Exeception
def get_name_input():
    name = str(input("Enter task name: "))
    return name


# gets task date from the user and returns date as a int
# TODO cehck input Exception
def get_date_input():
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    day = int(input("Enter day: "))
    return (year*10000) + (month*100) + day
