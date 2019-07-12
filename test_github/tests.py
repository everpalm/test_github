import unittest
from example import func1, func2

class ExampleTest(unitest.TestCase):
    @mock.patch('example.func1')
    def test_func2(self, mock_func1):
        mock_func1.return_value = 0
        self.assertEqual(func2(5), 25)
        mock_func1.return_value = 10
        self.assertEqual(func2(-5), -15)
