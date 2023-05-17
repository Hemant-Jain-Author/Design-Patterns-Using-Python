from abc import ABC, abstractmethod

class OrderPackingTemplate(ABC):
    
    def packProduct(self): # Final
        self.getProduct()
        self.addProductToBox()
        self.delivery()

    def getProduct(self):
        print("Get the product form shelf.")

    def addProductToBox(self):
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
o.packProduct()
print()
s = StoreOrderPacking()
s.packProduct()