import unittest
from test_mock_class1 import ExampleTest

if __name__ == '__main__':
    suite = unittest.TestSuite()

    #tests = [ExampleTest('test_func1'), ExampleTest('test_func2'), ExampleTest('test_func3')]
    
    suite.addTest(ExampleTest('test_func1'))
    suite.addTest(ExampleTest('test_func2'))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
