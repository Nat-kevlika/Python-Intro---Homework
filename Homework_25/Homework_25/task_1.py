import json
import os

def read_json_file(filename='dep_data.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except json.JSONDecodeError:
        print(f"Error: {filename} is not a valid JSON file.")
    except KeyError as e:
        print(f"Error: Missing key in JSON file - {e}")
    return None

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = float(salary)

class Department:
    def __init__(self, name, description, employees):
        self.name = name
        self.description = description
        self.employees = [Employee(**emp) for emp in employees]

    def average(self):
        if not self.employees:
            return 0
        total_salary = sum(emp.salary for emp in self.employees)
        return total_salary / len(self.employees)

    def max(self):
        if not self.employees:
            return 0
        return max(emp.salary for emp in self.employees)

    def min(self):
        if not self.employees:
            return 0
        return min(emp.salary for emp in self.employees)

    def positions(self):
        position_count = {}
        for emp in self.employees:
            if emp.position in position_count:
                position_count[emp.position] += 1
            else:
                position_count[emp.position] = 1
        return position_count

def main():
    file_path = 'dep_data.json'
    data = read_json_file(file_path)

    if data is None:
        return
    departments = []

    for key, value in data.items():
        department = Department(value['name'], value['description'], value['employees'])
        departments.append(department)
        print(f"Department: {department.name}")
        print(f"  Average Salary: {department.average()}")
        print(f"  Max Salary: {department.max()}")
        print(f"  Min Salary: {department.min()}")
        print(f"  Positions: {department.positions()}")

if __name__ == "__main__":
    main()
