
I created file named the file named student.py. 


$ python3.6 student.py 
User Alon has been added with id  0
User associated with id 0 is  Alon
$

Python unittest structure

Now, let’s learn how to code for unit testing. An individual testcase is created by subclassing unittest.TestCase. By overriding or adding appropriate functions, we can add logic to test. The following code will be succeeded if a is equals to b.


import unittest


class Testing(unittest.TestCase):
    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()

How to run python unittest module

