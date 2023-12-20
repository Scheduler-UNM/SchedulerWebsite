
import sqlite3
import os

class Shifts:
    def __init__(self):
        self.data_dir = "/workspaces/SchedulerWebsite/Data"

    def connect_to_database(self, db_filename):
        """Connect to the specified SQL database."""
        db_path = os.path.join(self.data_dir, db_filename)
        return sqlite3.connect(db_path)

    def get_next_shift_id(self, db_conn):
        """Get the next shift ID by finding the highest ID in the database and adding 1."""
        cursor = db_conn.cursor()
        cursor.execute("SELECT MAX(shift_id) FROM shifts")
        max_id = cursor.fetchone()[0]
        return (max_id or 0) + 1

    def get_id_for_value(self, db_conn, table, column, value):
        """Get the ID for a given value from the specified table."""
        cursor = db_conn.cursor()
        cursor.execute(f"SELECT id FROM {table} WHERE {column} = ?", (value,))
        result = cursor.fetchone()
        return result[0] if result else None

    def add_shift(self, db_conn, shift_id, term_id, time_of_shift, pod_id, num_of_scons, scon_id, repeat_times):
        """Add a shift to the database, repeating it a specified number of times."""
        cursor = db_conn.cursor()
        for _ in range(repeat_times):
            cursor.execute('''
                INSERT INTO shifts (shift_id, term_id, time_of_shift, pod_id, num_of_scons)
                VALUES (?, ?, ?, ?, ?)
            ''', (shift_id, term_id, time_of_shift, pod_id, num_of_scons))

            cursor.execute('''
                INSERT INTO employee_shifts (scon_id, shift_id)
                VALUES (?, ?)
            ''', (scon_id, shift_id))

        db_conn.commit()

    def create_shift(self, term, scon, pod, time_of_shift, num_of_scons, repeat_times):
        shifts_conn = self.connect_to_database("shifts.sql")
        shift_id = self.get_next_shift_id(shifts_conn)

        term_id = self.get_id_for_value(self.connect_to_database("term.sql"), "terms", "name", term)
        scon_id = self.get_id_for_value(self.connect_to_database("employee.sql"), "employees", "name", scon)
        pod_id = self.get_id_for_value(self.connect_to_database("pod.sql"), "pods", "name", pod)

        self.add_shift(shifts_conn, shift_id, term_id, time_of_shift, pod_id, num_of_scons, scon_id, repeat_times)
        shifts_conn.close()

# The following code will run only if this script is executed directly
if __name__ == "__main__":
    shifts_manager = Shifts()
    term = input("Enter the term (e.g., 'Spring', 'Summer', 'Fall'): ")
    scon = input("Enter the name of the scon (employee): ")
    pod = input("Enter the pod name: ")
    time_of_shift = input("Enter the time of the shift (e.g., '08:00 - 16:00'): ")
    num_of_scons = int(input("Enter the number of scons (employees) for the shift: "))
    repeat_times = int(input("How many times should this shift repeat?: "))

    shifts_manager.create_shift(term, scon, pod, time_of_shift, num_of_scons, repeat_times)
