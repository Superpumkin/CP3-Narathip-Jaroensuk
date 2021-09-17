class Customer :
    First_name = ''
    Last_name  = ''
    age = 0

    def addCart(self) :
        print(f"Added Product To {self.First_name } {self.Last_name} "+"'s cart" )

customer_1 = Customer()
customer_2 = Customer()
customer_3 = Customer()

#Customer 1
customer_1.First_name = 'Narathip'
customer_1.Last_name = 'J'
customer_1.age = 18
customer_1.addCart()

#Customer 2
customer_2.First_name = 'Thanawat'
customer_2.Last_name = 'P'
customer_2.age = 18
customer_2.addCart()

#Customer 3
customer_3.First_name = 'Preeyanuch'
customer_3.Last_name = 'C'
customer_3.age = 17
customer_3.addCart()