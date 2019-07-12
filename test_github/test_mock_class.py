import unittest
from unittest import mock
import example
#from example import Example as eg

#eg = Example(5)
#print("eg.func1() = %d, eg.func2() = %d" % (eg.func1(), eg.func2()))

''' Standard unittest function of class Example from example.py'''
'''
class ExampleTest(unittest.TestCase):
    def test_func2(self):
        self.assertEqual(example.Example(5).func1(), 25)
        self.assertEqual(example.Example(5).func2(), 0)
'''


class ExampleTest(unittest.TestCase):
    @mock.patch('example.Example.func1')
    def test_func2(self, mock_func1):
        mock_func1.return_value = 0
        self.assertEqual(example.Example(5).func2(),1)



#if __name__ == 'tests':
unittest.main()
    
