import unittest
from password import Credentials
from password import User
import pyperclip


class UserTest(unittest.TestCase):
    def setUp(self):
        '''
        method run before each user test
        '''
        self.new_user = User("Human", "orAmI?")

    def tearDown(self):
        '''
        method called after each user test
        '''
        User.data_user = []

    def test_init(self):
        '''
        test method to check if user class is initialized correctly
        '''
        self.assertEqual(self.new_user.owner,"Human")
        self.assertEqual(self.new_user.key, "orAmI?")
        
    def test_save_user(self):
        '''
        test method to test if user has been saved into class list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.data_user),1)

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

    def tearDown(self):
        """Method that cleans up after each case has run
        """
        Credentials.credential_list = []


    def test_save_credential(self):
        """To test if the credential is saved into the credential list
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credential_list),1)

    def test_save_multiple_credentials(self):
        """Test to check if we can save multiple credentials to our array
        """
        self.new_credential.save_credential()
        test_credential =  Credentials("twitter","password")

        test_credential.save_credential()
        self.assertEqual(len(Credentials.credential_list),2)

    def test_delete_credentials(self):
            '''
            test if we can remove a credential from our credential list
            '''
            self.new_credential.save_credential()
            test_credential = Credentials("twitter","password")
            test_credential.save_credential()

            self.new_credential.delete_credential()
            self.assertEqual(len(Credentials.credential_list),1)

    def test_find_credential_by_credential(self):
        '''
        test to check if we can find a credential by credential and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credentials("twitter","password")
        test_credential.save_credential()

        found_credential = Credentials.find_by_account("twitter")

        self.assertEqual(found_credential.password,test_credential.password)


    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential.
        '''

        self.new_credential.save_credential()
        test_credential = Credentials("twitter","password") # new credential
        test_credential.save_credential()

        credential_exists = Credentials.credential_exist("twitter")

        self.assertTrue(credential_exists)

        
        
    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credential_list)



    def test_copy_password(self):
        '''
        Test to confirm that we are copying the password from a found credential
        '''

        self.new_credential.save_credential()
        Credentials.copy_password("twitter")

        self.assertEqual(self.new_credential.password,pyperclip.paste())

if __name__ == '__main__':
    unittest.main()


