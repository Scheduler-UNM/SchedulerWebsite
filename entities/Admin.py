# admin.py
from Supervisor import Supervisor


class Admin(Supervisor):
    def __init__(self, staff_id, name, email):
        super().__init__(staff_id, name, email)
        self.employees = []  # List to manage employees
    def access_all_reports(self):
        print(f"{self.name} can access all reports.")

    def add_employee(self):
        print("Employee added.")

    def remove_employee(self):
        print("Removing Employee")

    def assign_shift(self, employee_id, shift):
        for employee in self.employees:
            if employee.staff_id == employee_id:
                employee.assign_shift(shift)
                print(f"Shift '{shift}' assigned to {employee.name}.")
                return
        print(f"No employee found with ID {employee_id}.")


    def deassign_shift(self, employee_id, shift):
        for employee in self.employees:
            if employee.staff_id == employee_id:
                employee.request_shift_giveaway(shift)
                print(f"Shift '{shift}' deassigned to {employee.name}.")
                return

        print(f"No employee found with ID {employee_id}.")



