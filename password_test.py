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


if __name__ == '__main__':
    unittest.main()


