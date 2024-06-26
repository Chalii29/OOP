class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0) :
        # Run validation to the received arguments
        assert price >= 0
        assert quantity >= 0


        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self) :
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self) :
        return f"Item('{self.name}', {self.price}, {self.quantity})"
item1 = Item("Phone", 100, 5)
#item1.apply_discount()
#print(item1.price)

item2 = Item("Laptop", 1000, 3)
#item2.pay_rate = 0.7
#item2.apply_discount()
#print(item2.price)

item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)


class Phone(Item):
    pass

phone1 = Item("Iphone", 500, 10)
phone1.broken_phones = 1
phone2 = Item("Samsung", 200, 3)
phone2.broken_phones = 1


#print(Item.all)

#for instance in Item.all:
 #print(instance.name)

#print(Item.__dict__) #All the attributes for class level
#print(item1.__dict__) #All the attributes for instance level