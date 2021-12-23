class Employee:
    """Collect information about an employee."""

    def __init__(self, first, last, salary):
        """Stores information and prepares for modifications."""
        self.first = first
        self.last = last
        self.salary = salary

    def begin_input(self):
        """Shows the information."""
        print("Please input information about an employee here.")

    def store_response(self, new_first, new_last, new_salary):
        """Stores new information in seperate lists."""
        self.first.append(new_first)
        self.last.append(new_last)
        self.salary.append(new_salary)

    def give_raise(self, current_salary, increase=5000):
        if increase == 0:
            print("You can't raise a salary by zero!")
        elif increase < 0:
            print("You can't raise a salary by a negative number!")
        else:
            updated_salary = current_salary + increase
            return updated_salary

    def show_results(self):
        """Show all the information that has been given."""
        self.first = [first.title() for first in self.first]
        self.last = [last.title() for last in self.last]
        print("Employee information:")
        for i in range(len(self.first)):
            print(f"{self.first[i]} {self.last[i]} - ${self.salary[i]}")