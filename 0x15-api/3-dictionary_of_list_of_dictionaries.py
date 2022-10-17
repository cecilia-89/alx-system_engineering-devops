#!/usr/bin/python3
"""returns information about an employee's todo list progress"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()


    with open("todo_all_employees.json", "w+") as f:
        json.dump({user.get('id'): [{
                  "task": todo.get('title'),
                  "completed": todo.get('completed'),
                  "username": user.get('username')}
                  for todo in todos] for user in users}, f)
