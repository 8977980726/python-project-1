import json
import os

EMPLOYEE_FILE = "employees.json"

# Load data from file if exists
def load_data():
    if os.path.exists(EMPLOYEE_FILE):
        with open(EMPLOYEE_FILE, "r") as f:
            return json.load(f)
    return {}

# Save data to file
def save_data(data):
    with open(EMPLOYEE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_employee(data):
    emp_id = input("Enter Employee ID: ")
    if emp_id in data:
        print("Employee ID already exists!")
        return
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    salary = input("Enter Salary: ")

    data[emp_id] = {"Name": name, "Department": dept, "Salary": salary}
    save_data(data)
    print("Employee added successfully!")

def view_employees(data):
    if not data:
        print("No employee records found.")
        return
    for emp_id, details in data.items():
        print(f"ID: {emp_id}, Name: {details['Name']}, "
              f"Dept: {details['Department']}, Salary: {details['Salary']}")

def update_employee(data):
    emp_id = input("Enter Employee ID to update: ")
    if emp_id not in data:
        print("Employee not found!")
        return
    print("Leave blank if you don’t want to change a field.")
    name = input(f"New Name ({data[emp_id]['Name']}): ") or data[emp_id]['Name']
    dept = input(f"New Department ({data[emp_id]['Department']}): ") or data[emp_id]['Department']
    salary = input(f"New Salary ({data[emp_id]['Salary']}): ") or data[emp_id]['Salary']

    data[emp_id] = {"Name": name, "Department": dept, "Salary": salary}
    save_data(data)
    print("Employee updated successfully!")

def delete_employee(data):
    emp_id = input("Enter Employee ID to delete: ")
    if emp_id not in data:
        print("Employee not found!")
        return
    del data[emp_id]
    save_data(data)
    print("Employee deleted successfully!")

def main():
    data = load_data()
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee(data)
        elif choice == "2":
            view_employees(data)
        elif choice == "3":
            update_employee(data)
        elif choice == "4":
            delete_employee(data)
        elif choice == "5":
            print("Exiting system... Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
