import example_class
import unittest
from unittest import mock 

class ExampleTest(unittest.TestCase):
    def test_func1(self):
        self.assertEqual(example_class.Example(0).func1(), 0)
        self.assertEqual(example_class.Example(1).func1(), 1)
        self.assertEqual(example_class.Example(-1).func1(), 0)

    @mock.patch('example_class.Example.func1')
    def test_func2(self, mock_func1):
        mock_func1.return_value = 1
        self.assertEqual(example_class.Example(1).func2(), 6)
        self.assertEqual(example_class.Example(-1).func2(), -4)
        self.assertEqual(example_class.Example(-0.2).func2(), 0)

    @mock.patch('example_class.Example.func1')
    @mock.patch('example_class.Example.func2')
    def test_func3(self, mock_func1, mock_func2):
        mock_func1.return_value = 1
        mock_func2.return_value = 1
        self.assertEqual(example_class.Example(1).func3(), 2)

if __name__ == '__main__':
    unittest.main()