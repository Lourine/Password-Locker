import unittest # Importing the unittest module
from user import User, Credentials# Importing the user and credential  class
import pyperclip

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Milly", "1234") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user_name,"Milly")
        self.assertEqual(self.new_user.password,"1234")
    
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []


    def test_save_user(self):
      """
      test case to test if a new user instance has been saved into the User list
      """
      self.new_user.save_user()
      self.assertEqual(len(User.user_list),1)

    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("user","1234") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("user","1234") # new user
            test_user.save_user()

            self.new_user.delete_user()# Deleting a contact object
            self.assertEqual(len(User.user_list),1)

    def test_user_exists(self):
      '''
      test to check if we can return a Boolean  if we cannot find the user.
      '''
      self.new_user.save_user()
      test_user = User("user","1234") # new user
      test_user.save_user()

      user_exists = User.user_exist("user")
      self.assertTrue(user_exists)


class TestCredentials(unittest.TestCase):
    """
    A test class that defines test cases for credentials class

    """ 
    def setUp(self):
        """
        Method that runs before each individual credentials test methods run.

        """
        self.new_credential = Credentials('Youtube','Millicent','1994milly')
    def test_init(self):
        """
        Test case to check if a new Credentials instance has been initialized correctly
        """
        self.assertEqual(self.new_credential.account,'Youtube')
        self.assertEqual(self.new_credential.userName,'Millicent')
        self.assertEqual(self.new_credential.password,'1994milly')
    
    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []
    
    def test_save_credentials(self):
        """
        test case to test if the credential object is saved into the credentials list.
        """
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self):
        '''
        test to check if we can save multiple credentials objects to our credentials list
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials("Twitter","Macharia","2017kare") 
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)
    
    def test_delete_credential(self):
        """
        test method to test if we can remove an account credentials from our credentials_list
        """
        self.new_credential.save_credentials()
        test_credential = Credentials("Twitter","Macharia","2017kare")
        test_credential.save_credentials()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credentials(self):
        """
        test to check if we can find a credential entry by account name and display the details of the credential
        """
        self.new_credential.save_credentials()
        test_credential = Credentials("Twitter","Macharia","2017kare") 
        test_credential.save_credentials()

        the_credential = Credentials.find_credential("Twitter")

        self.assertEqual(the_credential.account,test_credential.account)
    
    def test_credential_exist(self):
        """
        test to check if we can return a true or false based on whether we find or can't find the credential.
        """
        self.new_credential.save_credentials()
        the_credential = Credentials("Twitter","Macharia","2017kare")  
        the_credential.save_credentials()
        credential_is_found = Credentials.if_credential_exist("Twitter")
        self.assertTrue(credential_is_found)
    
    def test_display_all_saved_credentials(self):
        '''
        method that displays all the credentials that has been saved by the user
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

    def test_copy_credential(self):
        '''
        Test to confirm that we are copying the password  from a found credential
        '''

        self.new_credential.save_credentials()
        Credentials.copy_credential("Youtube")

        self.assertEqual(self.new_credential.account,pyperclip.paste())

  

if __name__ == '__main__':
    unittest.main()