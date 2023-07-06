from abc import ABC, abstractmethod

class OrderPackingTemplate(ABC):
    
    def pack_product(self): # Final
        self.get_product()
        self.add_product_tobox()
        self.delivery()

    def get_product(self):
        print("Get the product form shelf.")

    def add_product_tobox(self):
        print("Put the product inside Box.")
    
    @abstractmethod
    def delivery(self):
        pass


class OnlineOrderPacking(OrderPackingTemplate):
    def delivery(self):
        print("Add delivery address slip and ship.")

class StoreOrderPacking(OrderPackingTemplate):
    def delivery(self):
        print("Add thanks message to box and deliver to customer.")
  
# Client code. 
o = OnlineOrderPacking()
o.pack_product()
print()
s = StoreOrderPacking()
s.pack_product()