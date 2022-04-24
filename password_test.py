import unittest
from password import Credentials

class TestCredentials(unittest.TestCase):
    """test that defines test cases for the credential class behaviors

    Args:
        unittest.TestCase: class that helps in creating test cases
    """

    def setUp(self):
        """Setup method before each test case
        """
        self.new_credential = Credentials("twitter","password")


    def test_init(self):
        """Test if the object is initialized correctly
        """

        self.assertEqual(self.new_credential.account,"twitter")
        self.assertEqual(self.new_credential.password,"password")


if __name__ == '__main__':
    unittest.main()


# import unittest # Importing the unittest module
# from password import Credentials # Importing the contact class

# class TestCredentials(unittest.TestCase):

#     '''
#     Test class that defines test cases for the contact class behaviours.

#     Args:
#         unittest.TestCase: TestCase class that helps in creating test cases
#     '''



#     def setUp(self):
#         '''
#         Set up method to run before each test cases.
#         '''
#         self.new_credential = Credentials("James","Muriuki") # create contact object


#     def test_init(self):
#         '''
#         test_init test case to test if the object is initialized properly
#         '''

#         self.assertEqual(self.new_credential.account,"James")
#         self.assertEqual(self.new_credential.password,"Muriuki")
        


# if __name__ == '__main__':
#     unittest.main()