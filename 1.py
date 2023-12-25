class Product:
    #Class to store all the product Info
    def __init__(self, product_name,price,date_of_manufacturing,best_before,unique_id,product_quantity):
        self.product_name = product_name
        self.price = price
        self.date_of_manufacturing = date_of_manufacturing
        self.best_before = best_before
        self.unique_id = unique_id 
        self.product_quantity = product_quantity
        self.next_Product = None

class ShopCart:
    def __init__(self):
        self.head = None
        self.unique_id = 0

    #Function to add products in the List
    def addProduct(self, product_name,price,date_of_manufacturing,best_before,product_quantity):
        self.unique_id +=1
        print(f"Unique ID assigned to the product name - {product_name} is {self.unique_id}")
        new_Product = Product(product_name,price,date_of_manufacturing,best_before,self.unique_id,product_quantity)
        if self.head is None:
            self.head = new_Product
            return
        last_Product = self.head
        while last_Product.next_Product:
            last_Product = last_Product.next_Product
        last_Product.next_Product = new_Product
        if product_quantity <6:
            print(f"{product_name} is running Faster and Value is less than 6")

    # function is to removeDefective the product using Unique id 
    def removeDefective(self, unique_id):
        current_Product = self.head

        if current_Product and current_Product.unique_id == unique_id:
            self.head = current_Product.next_Product
            current_Product = None
            return

        prev_Product = None
        while current_Product and current_Product.unique_id != unique_id:
            prev_Product = current_Product
            current_Product = current_Product.next_Product

        if current_Product is None:
            return

        prev_Product.next_Product = current_Product.next_Product
        current_Product = None

    
    
    # function is to Display the products in the List
    def displayAll(self):
        current_Product = self.head
        while current_Product:
            print(current_Product.unique_id,current_Product.price,current_Product.product_name,current_Product.date_of_manufacturing,current_Product.best_before,current_Product.product_quantity)
            current_Product = current_Product.next_Product


    # function is to Display the product using Unique ID 
    def display(self,unique_id):
        current_Product = self.head
        while current_Product:
            if(current_Product.unique_id == unique_id):
                print(current_Product.unique_id,current_Product.price,current_Product.product_name,current_Product.date_of_manufacturing,current_Product.best_before,current_Product.product_quantity)
            current_Product = current_Product.next_Product
        print("Item Doesn't Exist")
    

# Example usage:
shop_cart = ShopCart()

#add in the format product_name,price,date_of_manufacturing,best_before)
from datetime import datetime
def validDate(user_input_date):
    user_date = datetime.strptime(user_input_date, "%Y-%m-%d")
    today = datetime.today()
    diff = today-user_date
    if int(diff.days)>=0:
        pass
    else:
        raise ValueError("Please Enter valid Date")



print('''Enter the function you want to perform: 
Choose between addProduct(AP),
DisplayAll(DA),
Display using Unique id(DUI),
Remove Defective Product(RDP),

(use 'stop' keyword to stop the program)''')
while True:
    function = input()
    if function.lower() == "stop":
        break
    if function.lower() == "ap":
        try:
            product_name = input("Enter the Product name : ")
            price = int(input("Enter the Product price : "))
            date_of_manufacturing = input("Enter the date of manufacturing : (YYYY/MM/DD)")
            validDate(date_of_manufacturing)
            best_before = input("Enter the best before : ")
            product_quantity =int(input("Enter the product quantity : "))
            shop_cart.addProduct(product_name,price,date_of_manufacturing,best_before,product_quantity)
        except Exception as e:
            print(e)

    elif function.lower() == "da":
        shop_cart.displayAll()

    elif function.lower() == "dui":
        try:
            unique_id = int(input("Enter the Unique id of the product : "))
            shop_cart.display(unique_id)
        except Exception as e:
            print(e)
    elif function.lower() == "rdp":
        try:
            unique_id = int(input("Enter the Unique id of the product : "))
            shop_cart.removeDefective(unique_id)
        except Exception as e:
            print(e)
    else:
        print("Invalid Input")
    

