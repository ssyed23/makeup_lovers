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


  def sign_in(self):
    if self.userList== []:
      print("There are no users in the application!")
    else:
      User_ID = int(input("Please enter your user ID to log in: "))
      if User_ID > len(self.userList):
        print('That user ID does not exist!')
      else:
        opened_acc=self.userList[int(User_ID)-1]
        print("\nWelcome "+ opened_acc.user_name + '!')
        


  def search_product(self):
    item_name = input("Please enter the brand you are interested in: ")
    try:
      self.app.search_prod(item_name)
      # search_product(item_name)
      
    except KeyError:
      print("That stock does not exist. Please enter a valid stock ticker!\n")
      return


  def save(self):
      self.app.save()

  def buy_product(self):
    self.app.purchase_items()

    
