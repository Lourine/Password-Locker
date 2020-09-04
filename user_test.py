import unittest # Importing the unittest module
from user import User # Importing the user class
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
            test_user = User("user","0712345678") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)


if __name__ == '__main__':
    unittest.main()