class Employee:
    def __init__(self, employee_id, name, position, salary=0):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Salary must be a positive number.")

    def display_details(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Position: {self.position}")


class EmployeeManagementSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self):
        employee_id = input("Enter Employee ID: ")
        if employee_id in self.employees:
            print("Employee ID already exists.")
            return

        name = input("Enter Name: ")
        position = input("Enter Position: ")

        salary_input = input("Enter Salary: ")
        if not salary_input.isdigit() or float(salary_input) <= 0:
            print("Salary must be a positive number.")
            return

        salary = float(salary_input)
        self.employees[employee_id] = Employee(employee_id, name, position, salary)
        print("Employee added successfully!")

    def display_employees(self):
        if not self.employees:
            print("No employees to display.")
        else:
            for employee in self.employees.values():
                employee.display_details()

    def update_salary(self):
        employee_id = input("Enter Employee ID: ")
        if employee_id not in self.employees:
            print("Employee not found.")
            return

        salary_input = input("Enter New Salary: ")
        if not salary_input.isdigit() or float(salary_input) <= 0:
            print("Salary must be a positive number.")
            return

        new_salary = float(salary_input)
        self.employees[employee_id].set_salary(new_salary)
        print("Salary updated successfully!")

    def view_salary(self):
        employee_id = input("Enter Employee ID: ")
        if employee_id not in self.employees:
            print("Employee not found.")
        else:
            salary = self.employees[employee_id].get_salary()
            print(f"Salary: {salary}")

    def run(self):
        while True:
            print("\n1. Add Employee")
            print("2. Display Employees")
            print("3. Update Salary")
            print("4. View Salary")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.display_employees()
            elif choice == "3":
                self.update_salary()
            elif choice == "4":
                self.view_salary()
            elif choice == "5":
                print("Exiting program. GoodBye!!")
                break
            else:
                print("Invalid choice. Please try again.")


# Create and run the system
system = EmployeeManagementSystem()
system.run()
