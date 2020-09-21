
class Users_C:
  
  def __init__(self, user_name, ID_num):
    
    self.user_name = user_name
    self.ID_num = ID_num
    self.port={}
  
  def __str__(self):
    
    return (f"Username: \"{self.user_name}\" | UserID:#{self.ID_num} " + f"{self.initial_investment:,.2f}") 
