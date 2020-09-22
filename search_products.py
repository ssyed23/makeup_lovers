import requests
import json
import boto3


class search_product:
  def __init__(self):
    self.brand_name = []
    self.init_response = []
    self.searched_history = []
    self.shopping_cart = []

    self.r = requests.get('https://makeup-api.herokuapp.com/api/v1/products.json?product_type=foundation')

  def search_prod(self, item_name):


    if self.r.status_code == 200:
          print('\nWe were able to find the brand you are looking for!')
    elif self.r.status_code == 404:
          print('Sorry we could not find the brand you are looking for, please try again!')
          return(self.search_product)

    
    data = self.r.json()
    
    print("Here are the products by " + item_name + ": ")
    self.brand_name.append(item_name)
    
    for i in range(0,166):
     if data[i]['brand'] == item_name:
       name_product = data[i]['name']
       price_product = data[i]["price"]
       product_link = data[i]["product_link"]
       product_id = data[i]["id"]

       print(name_product)
       print(price_product)
       print(product_link)
       print(product_id)


       
       
  def purchase_items(self):

    data = self.r.json()
    product_id = input("what is the name of the product you want to buy? ")
    quantity = int(input("How many would you like to add to your cart? "))

    for i in range(0,166):
      if data[i]['name'] == product_id:
        base_price = data[i]['price']
        total_price = float(base_price) * float(quantity)
        
        print(f"You purchased the item at a price of {base_price}"+ " each")
        print(f"Your total is {total_price}")
        values = (str(total_price), str(quantity), product_id)
        self.shopping_cart.append(values)


  

    for i in self.shopping_cart:
      print(i)

    
  
       
        # print(data[i]['id'])
        # print(data[i]['price'])
        

        #cost_of_item = data[i]['price']
        #print(cost_of_item)
    #self.shopping_cart.append(d)






    # print (r.json())
# print(r['price'])

