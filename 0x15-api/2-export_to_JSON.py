#!/usr/bin/python3
"""returns information about an employee's todo list progress"""
import requests
from sys import argv
import json

url = "https://jsonplaceholder.typicode.com/users/"

user = requests.get(url + "{}".format(argv[1])).json()
todos = requests.get(url + "{}/todos".format(argv[1])).json()
dic = {}
lst = []

for todo in todos:
    dic['task'] = todo.get('title')
    dic['completed'] = todo.get('completed')
    dic['username'] = user.get('username')
    lst.append(dic)

my_dict = {user.get('id'): lst}


with open("{}.json".format(user.get('id')), "w+") as f:
    json.dump(my_dict, f)
