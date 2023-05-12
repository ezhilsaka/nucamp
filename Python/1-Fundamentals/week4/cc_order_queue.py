class Queue:

    def __init__ (self):

        self.items = []
    
    def enqueue (self, value):
        
        self.items.append(value)

    def dequeue (self):

        if len(self.items) == 0:
            return None
        
        return self.items.pop(0)
    
    def size (self):

        return len(self.items)

class IceCreamShop:

    def __init__ (self, flavors):
        
        self.flavors = flavors
        self.orders = Queue()
    
    def take_order (self, customer, flavor, scoops):
        
        if flavor in self.flavors:
            
            if scoops >= 1 and scoops <= 3:

                print("Order created!")
                order = {"customer": customer, "flavor": flavor, "scoops": scoops}
                self.orders.enqueue(order)
            
            else:

                print("Choose the number of scoops between 1-3 scoops")
        else:

            print("Sorry, we don't have that flavor")
        
    def show_all_orders (self):

        all_orders = self.orders.items
        print("")
        print("All Pending Ice Cream Orders:")

        for items in all_orders:
            print("Customer: " + items["customer"] + " -- " + "Flavor: " + items["flavor"] + " -- " + "Scoops: " + str(items["scoops"]))
       
    def next_order (self):

        print("")
        print("Next Order up!")
        next_order = self.orders.dequeue()
        print("Customer: " + next_order["customer"] + " -- " + "Flavor: " + next_order["flavor"] + " -- " + "Scoops: " + str(next_order["scoops"]))

shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()