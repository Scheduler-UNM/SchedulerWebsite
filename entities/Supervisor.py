# supervisor.py
from Employee import Employee


class Supervisor(Employee):
    def approve_shifts(self):
        print(f"{self.name} can manage shifts.")


