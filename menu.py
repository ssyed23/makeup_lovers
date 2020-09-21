from application import Application
kik = Application()
to_Save = kik.userList

class Menu:
 def __init__(self):
    self.app = Application()
    self.options = {
      "1": self.app.add_user,
      "2": self.app.sign_in,
      "3": self.app.search_product,

    }

 def display_options(self):
      print(""" 
            ************* MAIN MENU *************
                       Welcome to Noorish! 
             
             Please choose from one of the options below:
 
             1. Create an account
             2. Sign In
             3. Continue as guest
             
 
             *************************************
 
             """)
 
 def run(self):
    while True:
      self.display_options()
      option = input("Please enter an option: ")
      action = self.options.get(option)

      if action:
        action()
      else:
        print("{0} is not a valid option, Please try again".format(option))
