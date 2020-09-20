import requests
import json
r = requests.get('https://makeup-api.herokuapp.com/api/v1/products.json?product_type=foundation')
print("____________________________")
# print (r.json())
# print(r['price'])

data = r.json()

print(len(data))
print(data[165])
print(data[165]['id'])


for i in range(0,166):
  print(data[i]['brand'])


item_name = input("Please enter the brand you are interested in: ")
print("Here are the products by " + item_name + ": ")
for i in range(0,166):
  if data[i]['brand'] == item_name:
    print(data[i]['name'])
    print("$ " + data[i]["price"])
    print(data[i]["product_link"])
    #print(data[i]['description'])

shopping_cart=[]
add_to_cart = input("Would you like to add this to your cart? ")
if add_to_cart == "yes":
  shopping_cart.append(data[i]["name"])
  with open('shopping_Cart.json', 'w') as output_file:
    new =json.dumps(shopping_cart,default=lambda o: o.__dict__, sort_keys=True, indent= 4)
    json.dump(new,output_file)





#def __init__(self):#,name):
 # base_url = "https://makeup-api.herokuapp.com/api/v1/products.json/product_type=foundation"
  #name = name.upper()
 # query_param = {"brand": name}
  #r = requests.get(base_url)#,query_param)
  #print (r)


