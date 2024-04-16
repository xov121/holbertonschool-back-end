#!/usr/bin/python3
"""
Fetches TODO list progress from JSONPlaceholder API and exports it to a CSV
file.
"""
import csv
import requests
import sys


def export_to_csv(employee_id):
    """
    Exports the TODO list progress for an employee to a CSV file.
    """
    base_url = 'https://jsonplaceholder.typicode.com'

    user_url = f'{base_url}/users/{employee_id}'
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Failed to fetch user details for ID: {employee_id}")
        return
    user_data = user_response.json()

    if 'name' not in user_data or 'id' not in user_data:
        print(f"No user found with ID: {employee_id}")
        return

    todos_url = f'{base_url}/todos?userId={employee_id}'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    csv_file_name = f"{employee_id}.csv"

    with open(csv_file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in todos_data:
            writer.writerow([employee_id, user_data['username'],
                             task['completed'], task['title']])

    print("Data for employee ID " + str(employee_id) +
          " has been written to " + csv_file_name)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            employee_id = int(sys.argv[1])
            export_to_csv(employee_id)
        except ValueError:
            print("Please provide a valid integer for the employee ID.")
    else:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
