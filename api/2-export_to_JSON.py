#!/usr/bin/python3
"""
Fetches TODO list progress from JSONPlaceholder API and exports it to a JSON
file.
"""
import json
import requests
import sys


def export_to_json(employee_id):
    """
    Exports the TODO list progress for an employee to a JSON file.
    """
    base_url = 'https://jsonplaceholder.typicode.com'

    user_url = f'{base_url}/users/{employee_id}'
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Failed to fetch user details for ID: {employee_id}")
        return
    user_data = user_response.json()

    if 'name' not in user_data or 'id' not in user_data \
       or 'username' not in user_data:
        print(f"No user found with ID: {employee_id}")
        return

    todos_url = f'{base_url}/todos?userId={employee_id}'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    tasks_info = []
    for task in todos_data:
        tasks_info.append({
            "task": task['title'],
            "completed": task['completed'],
            "username": user_data['username']
        })

    tasks_dict = {str(employee_id): tasks_info}

    json_file_name = f"{employee_id}.json"

    with open(json_file_name, 'w') as json_file:
        json.dump(tasks_dict, json_file)

    print("Data for employee ID " + str(employee_id) +
          " has been written to " + json_file_name)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            employee_id = int(sys.argv[1])
            export_to_json(employee_id)
        except ValueError:
            print("Please provide a valid integer for the employee ID.")
    else:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
