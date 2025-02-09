import tkinter as tk
from tkinter import messagebox, simpledialog

class Employee:
    def __init__(self, emp_id, name, department, position):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.position = position

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Department: {self.department}, Position: {self.position}"


class Report:
    def __init__(self):
        self.employees = {}

    def add_employee(self, employee):
        self.employees[employee.emp_id] = employee

    def find_by_id(self, emp_id):
        return self.employees.get(emp_id, None)

    def find_by_name(self, name):
        return [emp for emp in self.employees.values() if emp.name.lower() == name.lower()]

    def generate_report(self):
        return "\n".join(str(emp) for emp in self.employees.values())


class EmployeeManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.report = Report()

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Add Employee Section
        self.add_employee_frame = tk.Frame(self.root)
        self.add_employee_frame.pack(pady=10)

        tk.Label(self.add_employee_frame, text="Employee ID:").grid(row=0, column=0)
        self.emp_id_entry = tk.Entry(self.add_employee_frame)
        self.emp_id_entry.grid(row=0, column=1)

        tk.Label(self.add_employee_frame, text="Name:").grid(row=1, column=0)
        self.name_entry = tk.Entry(self.add_employee_frame)
        self.name_entry.grid(row=1, column=1)

        tk.Label(self.add_employee_frame, text="Department:").grid(row=2, column=0)
        self.department_entry = tk.Entry(self.add_employee_frame)
        self.department_entry.grid(row=2, column=1)

        tk.Label(self.add_employee_frame, text="Position:").grid(row=3, column=0)
        self.position_entry = tk.Entry(self.add_employee_frame)
        self.position_entry.grid(row=3, column=1)

        self.add_button = tk.Button(self.add_employee_frame, text="Add Employee", command=self.add_employee)
        self.add_button.grid(row=4, columnspan=2)

        # Search Section
        self.search_frame = tk.Frame(self.root)
        self.search_frame.pack(pady=10)

        tk.Label(self.search_frame, text="Search by ID:").grid(row=0, column=0)
        self.search_id_entry = tk.Entry(self.search_frame)
        self.search_id_entry.grid(row=0, column=1)

        self.search_id_button = tk.Button(self.search_frame, text="Search", command=self.search_by_id)
        self.search_id_button.grid(row=0, column=2)

        tk.Label(self.search_frame, text="Search by Name:").grid(row=1, column=0)
        self.search_name_entry = tk.Entry(self.search_frame)
        self.search_name_entry.grid(row=1, column=1)

        self.search_name_button = tk.Button(self.search_frame, text="Search", command=self.search_by_name)
        self.search_name_button.grid(row=1, column=2)

        # Report Section
        self.report_button = tk.Button(self.root, text="Generate Report", command=self.generate_report)
        self.report_button.pack(pady=10)

    def add_employee(self):
        emp_id = self.emp_id_entry.get()
        name = self.name_entry.get()
        department = self.department_entry.get()
        position = self.position_entry.get()

        if emp_id and name and department and position:
            employee = Employee(emp_id, name, department, position)
            self.report.add_employee(employee)
            messagebox.showinfo("Success", "Employee added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

    def search_by_id(self):
        emp_id = self.search_id_entry.get()
        employee = self.report.find_by_id(emp_id)
        if employee:
            messagebox.showinfo("Employee Found", str(employee))
        else:
            messagebox.showwarning("Not Found", "Employee not found.")

    def search_by_name(self):
        name = self.search_name_entry.get()
        employees = self.report.find_by_name(name)
        if employees:
            result = "\n".join(str(emp) for emp in employees)
            messagebox.showinfo("Employees Found", result)
        else:
            messagebox.showwarning("Not Found", "No employees found with that name.")

    def generate_report(self):
        report = self.report.generate_report()
        if report:
            messagebox.showinfo("Employee Report", report)
        else:
            messagebox.showwarning("No Employees", "No employees to report.")

    def clear_entries(self):
        self.emp_id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.department_entry.delete(0, tk.END)
        self.position_entry.delete(0, tk.END)
        self.search_id_entry.delete(0, tk.END)
        self.search_name_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagementSystem(root)
    root.mainloop()