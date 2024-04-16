#!/usr/bin/python3
"""
Fetches TODO list progress from JSONPlaceholder API for all employees
and exports it to a JSON file.
"""
import json
import requests


def export_all_to_json():
    """
    Exports the TODO list progress for all employees to a JSON file.
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    users_url = f'{base_url}/users'
    users_response = requests.get(users_url)
    users_data = users_response.json()

    all_tasks = {}

    for user in users_data:
        user_id = user['id']
        username = user['username']

        todos_url = f'{base_url}/todos?userId={user_id}'
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        user_tasks = []
        for task in todos_data:
            user_tasks.append({
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            })

        all_tasks[str(user_id)] = user_tasks

    json_file_name = "todo_all_employees.json"

    with open(json_file_name, 'w') as json_file:
        json.dump(all_tasks, json_file)

    print(f"Data for all employees has been written to {json_file_name}")


if __name__ == "__main__":
    export_all_to_json()
