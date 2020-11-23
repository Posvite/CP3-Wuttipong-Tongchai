class Customer:
    name = ""
    lastName = ""
    age = ""

    def addCart(self):
        print("Added Product to ",self.name,self.lastName,"'s cart")

customer1 = Customer()
customer1.name = "John"
customer1.lastName = "Snow"
customer1.addCart()

customer2 = Customer()
customer2.name = "John"
customer2.lastName = "Smith"
customer2.addCart()

customer3 = Customer()
customer3.name = "John"
customer3.lastName = "no John"
customer3.addCart()