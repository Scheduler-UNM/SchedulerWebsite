class Employee:
    def __init__(self, staff_id, name, email):
        self.staff_id = staff_id
        self.name = name
        self.email = email
        self.shifts = []


    def display_basic_info(self):
        print(f"Name: {self.name}, Email: {self.email}")


    def request_shifts(self, shift):
        print("Requesting shifts")


    def request_shift_swap(self, shift):
        print("Requesting swap")


    def request_shift_giveaway(self, shift):
        print("Requesting giveaway")

