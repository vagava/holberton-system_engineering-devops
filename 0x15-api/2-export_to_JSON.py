#!/usr/bin/python3
"""  Python script to export data in the JSON format. """
import json
import requests
import sys

if __name__ == "__main__":
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()

    new_file = "{}.json".format(sys.argv[1])

    for i in users:
        if i.get("id") == int(sys.argv[1]):
            name = i.get("username")

    list_of_task = []
    for i in todos:
        if i.get("userId") == int(sys.argv[1]):
            info_task = {}
            info_task["task"] = i.get("title")
            info_task["completed"] = i.get("completed")
            info_task["username"] = name
            list_of_task.append(info_task)
    employee_task_information = {}
    employee_task_information[sys.argv[1]] = list_of_task
    with open(new_file, 'w') as f:
        jsonobject = json.dumps(employee_task_information)
        f.write(jsonobject)
