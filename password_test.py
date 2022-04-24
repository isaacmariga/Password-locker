from cgi import test
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

    def test_find_credential_by_account(self):
        '''
        test to check if we can find a credential by account and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credentials("twitter","password")
        test_credential.save_credential()

        found_credential = Credentials.find_by_account("twitter")

        self.assertEqual(found_credential.password,test_credential.password)


if __name__ == '__main__':
    unittest.main()


