
I created file named the class file as student.py. 


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

If you’re using PyCharm IDE, you can simply press ctrl+shift+F10 to run unittest module. Otherwise you can use command prompt to run this module. For example, we named the file for unit-testing as Basic_Test.py. So the command to run python unittest will be:


$python3.6 -m unittest Basic_Test.Testing

If you want to see the verbose, then the command will be;


$python3.6 -m unittest -v Basic_Test.Testing

By using the PyCharm, we get the below output.

Python unittest, python unit test example
Python Unit Test Outcome & Basic Functions

This unittest has 3 possible outcomes. They are mentioned below:

    OK: If all test cases are passed, the output shows OK.
    Failure: If any of test cases failed and raised an AssertionError exception
    Error: If any exception other than AssertionError exception is raised. 

There are several function under unittest module. They are listed below.
Method 	Checks that
assertEqual(a,b) 	a==b
assertNotEqual(a,b) 	a != b
assertTrue(x) 	bool(x) is True
assertFalse(x) 	bool(x) is False
assertIs(a,b) 	a is b
assertIs(a,b) 	a is b
assertIsNot(a, b) 	a is not b
assertIsNone(x) 	x is None
assertIsNotNone(x) 	x is not None
assertIn(a, b) 	a in b
assertNotIn(a, b) 	a not in b
assertIsInstance(a, b) 	isinstance(a, b)
assertNotIsInstance(a, b) 	not isinstance(a, b)
Python unit test example

Now it’s time to write unit tests for our source class Person. In this class we have implemented two function – get_name() and set_name().

Now, we will test those function using unittest. So we have designed two test cases for those two function. Have a look at the following code, you will understand it easily.


import unittest

# This is the class we want to test. So, we need to import it
import Person as PersonClass


class Test(unittest.TestCase):
    """
    The basic class that inherits unittest.TestCase
    """
    person = PersonClass.Person()  # instantiate the Person Class
    user_id = []  # variable that stores obtained user_id
    user_name = []  # variable that stores person name

    # test case function to check the Person.set_name function
    def test_0_set_name(self):
        print("Start set_name test\n")
        """
        Any method which starts with ``test_`` will considered as a test case.
        """
        for i in range(4):
            # initialize a name
            name = 'name' + str(i)
            # store the name into the list variable
            self.user_name.append(name)
            # get the user id obtained from the function
            user_id = self.person.set_name(name)
            # check if the obtained user id is null or not
            self.assertIsNotNone(user_id)  # null user id will fail the test
            # store the user id to the list
            self.user_id.append(user_id)
        print("user_id length = ", len(self.user_id))
        print(self.user_id)
        print("user_name length = ", len(self.user_name))
        print(self.user_name)
        print("\nFinish set_name test\n")

    # test case function to check the Person.get_name function
    def test_1_get_name(self):
        print("\nStart get_name test\n")
        """
        Any method that starts with ``test_`` will be considered as a test case.
        """
        length = len(self.user_id)  # total number of stored user information
        print("user_id length = ", length)
        print("user_name length = ", len(self.user_name))
        for i in range(6):
            # if i not exceed total length then verify the returned name
            if i < length:
                # if the two name not matches it will fail the test case
                self.assertEqual(self.user_name[i], self.person.get_name(self.user_id[i]))
            else:
                print("Testing for get_name no user test")
                # if length exceeds then check the 'no such user' type message
                self.assertEqual('There is no such user', self.person.get_name(i))
        print("\nFinish get_name test\n")


if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()

Note that the unittest module executes the test functions in the order of their name, not in the order they are defined. And since we want our set_name test to execute first, we have named our test case functions as test_0_set_name and test_1_get_name.
Python Unit Test Example Output

Below images show the output produced by our unit test program – both in normal mode and in verbose mode.

Python unit test example

python unittest tutorial


$ python3.6 -m unittest -v PersonTest.Test
test_0_set_name (PersonTest.Test) ... Start set_name test

user_id length =  4
[0, 1, 2, 3]
user_name length =  4
['name0', 'name1', 'name2', 'name3']

Finish set_name test

ok
test_1_get_name (PersonTest.Test) ... 
Start get_name test

user_id length =  4
user_name length =  4
Testing for get_name no user test
Testing for get_name no user test

Finish get_name test

ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
$

That’s all about Python unittest tutorial. To learn more, read the Official Documentation. For any further query please use the comment box. 🙂
Facebook
Twitter
WhatsApp
Reddit
Linkedin
Email

    Prev

    Python zip() function

    Next

    Python Socket Programming - Server, Client Example

Pankaj

I love Open Source technologies and writing about my experience about them is my passion.

Follow Author

Comments

    Simon
    says:	
    June 5, 2018 at 2:45 am

    Hi!

    After running:
    $python3.6 -m unittest Basic_Test.Testing

    I get the following error:
    “ERROR: Basic_Test (unittest.loader._FailedTest)
    ———————————————————————-
    ImportError: Failed to import test module: Basic_Test
    Traceback (most recent call last):
    File “C:\Users (…) loader.py”, line 154, in loadTestsFromName
    module = __import__(module_name)
    ModuleNotFoundError: No module named ‘Basic_Test’

    What did I do wrong?
    Reply
        Pankaj
        says:	
        June 5, 2018 at 2:52 am

        Check if your python script name is Basic_Test.py? Also it has to be in the same directory.
        Reply

Leave a Reply

Your email address will not be published. Required fields are marked *

Comment

Name *

Email *

