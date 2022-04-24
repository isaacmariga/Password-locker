class Credentials:
    """
    Class that generates instances of credentials
    
    """
    credential_list = []

    def __init__(self, account, password):
        """
        Method that defines the properties of our credentials

        """
        self.account = account
        self.password = password

    def save_credential(self):
        """method saves credential objects into credential_list
        """
        Credentials.credential_list.append(self)


    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credentials.credential_list.remove(self)


    
    @classmethod
    def find_by_account(cls, account):
        '''
        Method that takes in an account and returns its password.

        '''

        for credential in cls.credential_list:
            if credential.account == account:
                return credential
