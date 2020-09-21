import requests
import json

class search_product:
  def __init__(self):
    self.brand_name = []
    self.init_response = []
    self.searched_history = []
    self.shopping_cart = []

    self.r = requests.get('https://makeup-api.herokuapp.com/api/v1/products.json?product_type=foundation')

    def search_prod(self, item_name):


    if self.r.status_code == 200:
          print('\nWe were able to find the value of the stock!')
    elif self.r.status_code == 404:
          print('Sorry we could not find the stock you were looking for')
          return(self.search_product)

    
    data = self.r.json()

    # self.init_response.append(data)

    # print(data)
    #print(data[165])
    #print(data[165]['id'])
    

    # print(len(data))


    # for i in range(0,166):
    #   print(data[i]['brand'])
    
    #item_name = input("Please enter the brand you are interested in: ")
    


#print(len(data))
#print(data[165])
#print(data[165]['id'])


#for i in range(0,166):
  #print(data[i]['brand'])


#item_name = input("Please enter the brand you are interested in: ")

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

    self.purchase_items()
       
       
  def purchase_items(self):

    data = self.r.json()
    product_id = input("what is the id of the product you want to buy ? ")
    how_many = int(input("quantitiety: "))

    for i in range(0,166):
      if data[i]['name'] == product_id:
        print(data[i]['id'])
        print(data[i]['price'])
        print(data[i]['link'])

        cost_of_item = data[i]['price']
        print(cost_of_item)







    # print (r.json())
# print(r['price'])

