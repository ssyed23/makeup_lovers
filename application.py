from users import Users_C
from search_products import search_product
import sys
import json

class Application:
  
  def __init__(self):
    self.ID=1
    self.userList=[] #dictionary of accounts (connects with portfolio)
    self.app = search_product()

  def add_user(self):
    account_name = input(str(f"What is the name of the user? : "))
    ID = self.ID
    user_input = Users_C(account_name, ID)
    self.userList.append(user_input)
    print("\nAccount created!\nYour username is \""+ str(account_name) + "\" and your personal user id is \"" + str(ID) + "\"")
    self.ID +=1
