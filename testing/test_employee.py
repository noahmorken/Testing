import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee."""

    def setUp(self):
        self.employee_list = Employee([], [], [])
        self.first = ['John', 'Clive', 'Arthur']
        self.last = ['Tolkien', 'Lewis', 'Doyle']
        self.salary = [300000, 250000, 200000]
        
    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.employee_list.store_response(self.first[0], self.last[0], self.salary[0])
        self.assertIn(self.first[0], self.employee_list.first)
        self.assertIn(self.last[0], self.employee_list.last)
        self.assertIn(self.salary[0], self.employee_list.salary)

    def test_give_default_raise(self):
        """Test that the default raise is added properly."""
        self.employee_list.store_response(self.first[0], self.last[0], self.salary[0])
        new_salary = int(self.salary[0]) + 5000
        self.assertEqual(new_salary, self.employee_list.give_raise(self.salary[0]))

    def test_give_custom_raise(self):
        """Test that a custom raise is added properly."""
        self.employee_list.store_response(self.first[0], self.last[0], self.salary[0])
        new_salary = int(self.salary[0]) + 10000
        self.assertEqual(new_salary, self.employee_list.give_raise(self.salary[0], 10000))

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for i in range(0, 3):
            self.employee_list.store_response(self.first[i], self.last[i], self.salary[i])
            self.assertIn(self.first[i], self.employee_list.first)
            self.assertIn(self.last[i], self.employee_list.last)
            self.assertIn(self.salary[i], self.employee_list.salary)

if __name__ == '__main__':
    unittest.main()