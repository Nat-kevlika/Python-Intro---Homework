import json

def calc_aver_salary(data):
    avg_salaries = {}

    for department, info in data.items():
        employees = info.get('employees', [])
        valid_salaries = []
        for emp in employees:
            try:
                salary = float(emp.get('salary'))
                valid_salaries.append(salary)
            except (TypeError, ValueError):
                pass

        if valid_salaries:
            avg_salaries[department] = sum(valid_salaries) / len(valid_salaries)
        else:
            avg_salaries[department] = 0

    return avg_salaries

def main():
    try:
        with open('homework_1.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("File not found.")
        return
    except json.JSONDecodeError:
        print("Wrong JSON format")
        return
    except ValueError:
        print("You must enter integer value")
        return

    avg_salaries = calc_aver_salary(data)

    for department, avg_salary in avg_salaries.items():
        print(f"{department}: {avg_salary}")

    with open('avg_salary.json', 'w') as file:
        json.dump(avg_salaries, file, indent = 4)

if __name__ == "__main__":
    main()
