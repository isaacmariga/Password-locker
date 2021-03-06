#!/usr/bin/env python3.9

from password import Credentials
from password import User
import pyfiglet

def create_user(owner, key):
    '''
    function to create a new user
    '''
    new_user = User(owner, key)
    return new_user

def save_user(data):
    '''
    function to save a new user
    '''
    data.save_user()

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
    credential.save_credential()


def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()


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
    return Credentials.display_credentials()


def copy_password():
    '''
    Function that copies password to clipboard
    '''
    return Credentials.display_credentials()



def main():

    print("     ____                                     _   _               _             ")       
    print("    |  _ \ __ _ ___ ___ __      _____  _ __ __| | | |    ___   ___| | _____ _ __ ")
    print("    | |_) / _` / __/ __ \ \ /\ / / _ \| '__/ _` | | |   / _ \ / __| |/ / _ \ '__|")
    print("    |  __/ (_| \__ \__ \ \ V  V / (_) | | | (_| | | |__| (_) | (__|   <  __/ |   ")
    print("    |_|   \__,_|___/___/  \_/\_/ \___/|_|  \__,_| |_____\___/ \___|_|\_\___|_|   ")
                                                                           
    
    print("\n""Hello Welcome to your Password-locker. What would you like to do?")
    
    print("\n 1. Create an account \n 2 Exit")
    option = input()


    if option == "1":
            print("\n" "what is your name?")
            
            owner = input()
            if not owner:
                print("\n" "You must type in something")
            else:
                print("\n""Enter password")
                key = input()
                if not owner:
                        print("\n""You must type in something")
                else:
                        save_user(create_user(owner, key))
                        print("-"*10)
                        print("\n"f"{owner} please enter your password again to enter")
                        new_key = input()
                        if new_key == key:
                                print("\n You have successfully logged in")


                        while True:
                            print("\n""Use these short codes : \n cc - create a new credential, \n dc - display credentials, \n fc -find a credential, \n ex -exit the password-locker")
                            short_code = input().lower()
                            if short_code == 'cc':
                                print("\n""New Credential")
                                print("-"*10)
                                print("\n""Account ....")
                                account = input()
                                print("\n""Password...")
                                passsword = input()

                                # create and save new credential.
                                save_credentials(create_credential(account, passsword))
                                print('\n')
                                print(f"New Credential {account} {passsword} created")
                                print('\n')
                            elif short_code == 'dc':
                                if display_credentials():
                                    print("Here is a list of all your credentials")

                                    print('\n')

                                    for credential in display_credentials():
                                    
                                        print(f"Account: {credential.account} Password:{credential.password}")
                                    print('\n')
                                else:
                                    print('\n')
                                    print("You dont seem to have any credentials saved yet")
                                    print('\n')
                            elif short_code == 'fc':
                                print("Enter the account you want to search for")

                                search_account = input()

                                if check_existing_credentials(search_account):
                                    search_credential = find_credential(search_account)
                                    print(f"Your {search_credential.account} Password is: {search_credential.password}")
                                    print('-' * 20)
                                else:
                                    print("\n""That credential does not exist")
                            elif short_code == "ex":
                                print("\n""Bye .......")
                                break
                            else:
                                print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()