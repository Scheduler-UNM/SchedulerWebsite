from Admin import Admin
from Supervisor import Supervisor
from Employee import Employee

# Creating instances
admin = Admin(1, "Alice", "alice@example.com")
supervisor = Supervisor(2, "Bob", "bob@example.com")
employee = Employee(3, "Charlie", "charlie@example.com")

# Using methods from various levels
admin.display_basic_info()  # From Employee
#admin.manage_shifts()       # From Supervisor
admin.access_all_reports()  # From Admin

supervisor.display_basic_info()  # From Employee
#supervisor.manage_shifts()       # From Supervisor

employee.display_basic_info()    # From Employee
#employee.request_shifts()
#supervisor.request_shift_swap()