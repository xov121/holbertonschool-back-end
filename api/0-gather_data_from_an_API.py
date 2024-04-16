#!/usr/bin/python3
import requests
import sys


def fetch_data(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'

    user_url = f'{base_url}/users/{employee_id}'
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Failed to fetch user details for ID: {employee_id}")
        return
    user_data = user_response.json()

    if 'name' not in user_data:
        print(f"No user found with ID: {employee_id}")
        return

    todos_url = f'{base_url}/todos?userId={employee_id}'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    completed_tasks = sum(task['completed'] for task in todos_data)

    print("Employee " + user_data['name'] + " is done with tasks(" +
          f"{completed_tasks}/{total_tasks}):")

    for task in todos_data:
        if task['completed']:
            print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            employee_id = int(sys.argv[1])
            fetch_data(employee_id)
        except ValueError:
            print("Please provide a valid integer for the employee ID.")
    else:
        print("Usage: ./0-gather_data_fron_an_API.py <employee_id>")
