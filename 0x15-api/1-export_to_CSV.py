#!/usr/bin/python3
"""using a REST API, for a given employee ID, returns information about
his/her TODO list progress"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    """Your code should not be executed when imported"""

    user_id = argv[1]

    todos = requests.get(
        "http://jsonplaceholder.typicode.com/todos?userId={}".format(
            user_id))
    user = requests.get(
        "http://jsonplaceholder.typicode.com/users/{}".format(
            user_id))

    with open('{}.csv'.format(user_id), "w") as output:
        writer = csv.writer(output, delimiter=',', quoting=csv.QUOTE_ALL)
        for tarea in todos.json():
            data = [
                user.json().get('id'),
                user.json().get('username'),
                tarea.get('completed'),
                tarea.get('title')
            ]
            writer.writerow(data)
