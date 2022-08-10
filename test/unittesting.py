import unittest
from user import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('sam', 'kike')
        self.assertEqual(formatted_name, 'Sam Kike')
unittest.main()