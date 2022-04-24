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
    print("Hello Welcome to your Password-locker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new credential, dc - display credentials, fc -find a credential, ex -exit the password-locker")
        short_code = input().lower()
        if short_code == 'cc':
            print("New Credential")
            print("-"*10)
            print("Account ....")
            account = input()
            print("Password...")
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
                print("That credential does not exist")
        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()