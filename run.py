#!/usr/bin/env python3.6
from user import User, Credentials
import secrets
import string

def create_new_user(user_name,password):
    '''
    Function to create a new user with a username and password
    '''
    new_user = User(user_name,password)
    return new_user

def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()

def display_user():
    """
    Function to display existing user
    """
    return User.display_user()

def login_user(username,password):
    """
    function that checks whether a user exist and then login the user in.
    """
  
    check_user = User.user_exist(username)
    return check_user

def create_new_credential(account,userName,password):
    """
    Function that creates new credentials for a given user account
    """
    new_credential = Credentials(account,userName,password)
    return new_credential
def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    credentials. save_credentials()
def display_accounts_details():
    """
    Function that returns all the saved credential.
    """
    return Credentials.display_credentials()

def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list

    """
    credentials.delete_credentials()

def find_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credentials.find_credential(account)
def check_credentials(account):
    """
    Function that check if a Credentials exists with that account name and return true or false

    """
    return Credentials.if_credential_exist(account)
def generate_password(psw_len):
    '''
    generate a new password
    Args:
    psw_len: preffered password length
    '''

    return "".join(secrets.choice(string.ascii_letters+string.digits) for i in range(psw_len))

def copy_credential(account):
    """
    A function that copies the password using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    """
    return Credentials.copy_credential(account)



def main():
    print("Hello Welcome to your Pass Word Locker. What is your name?")
    user_name = input()
    print(f"Hello {user_name}, sign up to Pass Word Locker to create an account.")
    print('\n')
    while True:
        print("Use these known short codes to operate :\n SU -> SIGN UP.\n LG ->LOGIN.\n ex ->exit Pass Word Locker. ")
        short_code = input().lower()
        if short_code == 'su':
            print("Create a Pass Word Locker Account")
            print("_"*100)
            u_name = input('User name:')
            print ('\n')
            pwd = input('Password : ')
            print ('\n')
            save_user(create_new_user(u_name,pwd)) 
            print ('\n')
            print(f"A New Password Locker Account with the user name  {u_name} has been created.")
            print(f"You can now login to your  account using your password.")
            print ('\n')
        elif short_code == "lg":
            print("*"*50)
            print("Enter your User name and your Password to log in:")
            print('*' * 50)
            default_username = input("User name: ")
            default_password = input("password: ")
            print('\n')
            while default_username!= u_name or default_password!= pwd:
                print("Wrong UserName or Password.")
                print("Enter username")
                default_username = input()
                print("Enter Password")
                default_password = input()
                print("\n")
            else:
                print ("Login Success")
                print("\n")
                print("\n")
                print(f"Hello {default_username}.Welcome To PassWord Locker Manager")  
                print('\n')
                while True:
                    print("Use these short codes:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A randomn password \n CP - Copy Credentials \n D - Delete credential \n EX - Exit the application \n")
                    short_code = input().lower().strip()
                    if short_code == "cc":
                        print("Create New Credential")
                        print("."*20)
                        print("Account name ....")
                        account = input().lower()
                        print("Your Account username")
                        userName = input()
                        print('Password: ')
                        print('Would you like us to automatically generate you a password? y/n')
                        ps = input().lower()
                        if ps == 'y':
                            print('Enter your preferred password length')
                            ps_len = int(input())
                            password = generate_password(ps_len)
                            print(f'Your new password for {account} is {password}')
                        elif ps == 'n':
                            print('Create your password: ')
                            password = input()

                        else:
                            print('Invalid choice!')
                        save_credentials(create_new_credential(account,userName,password))
                        print('\n')
                        print(f"Account Credential for: {account} - UserName: {userName} - Password:{password} created succesfully")
                        print('\n')
                    elif short_code == "dc":
                        if display_accounts_details():
                            print("Here's your list of accounts: ")
                            print('*' * 30)
                            print('_'* 30)
                            for account in display_accounts_details():
                                print(f" Account:{account.account} \n User Name:{userName}\n Password:{password}")
                                print('_'* 30)
                                print('*' * 30)
                        else:
                            print("You don't have any credentials saved yet..........")
                    elif short_code == "fc":
                        print("Enter the Account Name you want to search for")
                        search_name = input().lower()
                        if find_credential(search_name):
                            search_credential = find_credential(search_name)
                            print(f"Account Name : {search_credential.account}")
                            print('-' * 50)
                            print(f"User Name: {search_credential.userName} Password :{search_credential.password}")
                            print('-' * 50)
                        else:
                            print("That Credential does not exist")
                            print('\n')
                    elif short_code == "d":
                        print("Enter the account name of the Credentials you want to delete")
                        search_name = input().lower()
                        if find_credential(search_name):
                            search_credential = find_credential(search_name)
                            print("_"*50)
                            search_credential.delete_credentials()
                            print('\n')
                            print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                            print('\n')
                        else:
                            print("That Credential you want to delete does not exist in your store yet")

                    elif short_code == 'gp':
                        ps_len = int(input())
                        password = generate_password(ps_len)
                        print(f" {password} Has been generated succesfull. You can proceed to use it to your account")

                    elif short_code == 'cp':
                            print('Enter the account of the credentials whose details you want to copy')
                            search_account = input()
                            if check_credentials(search_account):
                                copy_credential(search_account)
                                print('Credential has been copied')
                            else:
                                print('Please enter a valid account')

                    elif short_code == 'ex':
                        print("Thanks for using passwords store manager.. See you next time!")
                        break
                    else:
                        print("Wrong entry... Check your entry again and let it match those in the menu")
                
        elif short_code == "ex":
                    print(f"Thanks {user_name} for your time.I hope you enjoyed my service.Bye...")
                    break    
        else:
            print("I really didn't get that. Please use the short codes")
           

if __name__ == '__main__':
    main()