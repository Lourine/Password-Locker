class User:
    """
    User class that generates new instances of a User
    """
    user_list = [] #empty User List
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
  
    def save_user(self):
        """
        Save User Method saves a new user to the user_List
        """
        User.user_list.append(self)
  
    def delete_user(self):
        '''
        delete_user method deletes a saved user from the user_list
        '''
        User.user_list.remove(self)
        
    @classmethod
    def display_user(cls):
        return cls.user_list

    @classmethod
    def user_exist(cls,user_name):
        '''
        Method that checks if a user exists from the user list.
        Args:
        string: User_name to search if it exists
        Returns :
        Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.user_name == user_name:
                return True
        return False


#Create the 2nd class
class Credentials():
    """
    Create credentials class to help create new objects of credentials
    """
    credentials_list = [] #empty credential list
    def __init__(self,account,userName, password):
        """
        method that defines user credentials to be stored
        """
        self.account = account
        self.userName = userName
        self.password = password

    def save_credentials(self):
        """
        method to store a new credential to the credentials list
        """
        Credentials.credentials_list.append(self)
    
    def delete_credentials(self):
        """
        delete_credentials method that deletes an account credentials from the credentials_list
        """
        Credentials.credentials_list.remove(self)