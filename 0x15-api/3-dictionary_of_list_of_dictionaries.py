#!/usr/bin/python3
"""  Python script to export data in the JSON format. """

import json
import requests
import sys

if __name__ == "__main__":
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()

    all_employees = {}
    for user in users:
        list_of_task = []
        for i in todos:
            if i.get("userId") == user.get("id"):
                info_task = {}
                info_task["task"] = i.get("title")
                info_task["completed"] = i.get("completed")
                info_task["username"] = user.get("username")
                list_of_task.append(info_task)
        all_employees[user.get("id")] = list_of_task

    with open("todo_all_employees.json", 'w') as f:
        jsonobject = json.dumps(all_employees)
        f.write(jsonobject)
