#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
returns information about his/her TO DO list progress. """

import requests
import sys

if __name__ == "__main__":
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()

    tasks = ""
    number_tasks = 0
    done_task = 0
    tasks = ""
    # find number total of task and number of done task
    for i in todos:
        if i.get("userId") == int(sys.argv[1]):
            number_tasks += 1
            if i.get("completed") is True:
                done_task += 1
                tasks += "\t " + i.get("title") + "\n"
    # find the name of employe
    for i in users:
        if i.get("id") == int(sys.argv[1]):
            name = i.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(name, done_task, number_tasks))
    print(tasks, end="")
