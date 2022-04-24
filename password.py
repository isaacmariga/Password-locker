class Credentials:
    """
    Class that generates instances of credentials
    
    """
    credentials = []

    def __init__(self, account, password):
        """
        Method that defines the properties of our credentials

        """
        self.account = account
        self.password = password
