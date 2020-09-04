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
    Save User Method saves a new user to the User_List
    """
    User.user_list.append(self)