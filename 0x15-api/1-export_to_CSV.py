#!/usr/bin/python3
""" Python script to export data in the CSV format."""

import csv
import requests
import sys

if __name__ == "__main__":
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()

    new_file = "{}.csv".format(sys.argv[1])
    # find the name of employe
    for i in users:
        if i.get("id") == int(sys.argv[1]):
            name = i.get("username")
    # create new file
    with open(new_file, 'w') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        for i in todos:
            if i.get("userId") == int(sys.argv[1]):
                w.writerow([sys.argv[1], name,
                            i.get("completed"), i.get("title")])
