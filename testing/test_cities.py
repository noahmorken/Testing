import unittest
from city_function import format_city

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py"""

    def test_city_country(self):
        """Do inputs like 'Zagreb, Croatia' work?"""
        formatted_city = format_city('zagreb', 'croatia')
        self.assertEqual(formatted_city, 'Zagreb, Croatia')

    def test_city_country_population(self):
        """Do inputs like 'Dhaka, Bangladesh, 8906000' work?"""
        formatted_city = format_city('zagreb', 'croatia', '8906000')
        self.assertEqual(formatted_city, 'Zagreb, Croatia - Population 8906000')

if __name__ == '__main__':
    unittest.main()