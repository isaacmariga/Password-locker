#!/usr/bin/env python3.9

from password import Credentials


def create_credential(account, password):
    '''
    Function to create a new credential
    '''
    new_credential = Credentials(account, password)
    return new_credential


def save_credentials(credential):
    '''
    Function to save credential
    '''
    Credentials.save_credential()

def del_credential(credential):
    '''
    Function to delete a credential
    '''
    Credentials.delete_credential()

def find_credential(account):
    '''
    Function that finds a credential by account and returns the credential
    '''
    return Credentials.find_by_account(account)

def check_existing_credentials(account):
    '''
    Function that check if a credential exists with that account and return a Boolean
    '''
    return Credentials.credential_exist(account)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return save_credentials.display_credentials()