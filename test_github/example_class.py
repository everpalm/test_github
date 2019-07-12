class Example:
    def __init__(self, x):
        self.x = x

    def func1(self):
        return self.x**2

    def func2(self):
        return self.func1() + self.x*5

    def func3(self):
        return self.func1() + self.func2()

    #this is a test
