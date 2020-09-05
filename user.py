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

