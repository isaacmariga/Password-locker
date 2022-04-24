#!/usr/bin/env python3.9

from password import Credentials

def create_credential(account, password):
    '''
    Function to create a new credential
    '''
    new_credential = Credentials(account,password)
    return new_credential