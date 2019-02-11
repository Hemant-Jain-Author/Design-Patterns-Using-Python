from abc import ABC, abstractmethod

class CreditCard(ABC):
    @abstractmethod
    def name(self):
        pass
    
    @abstractmethod
    def accept(self, visitor):
        pass

class BronzeCreditCard(CreditCard):
    def name(self):
        return "BronzeCreditCard"    
        
    def accept(self, visitor):
        cashback = visitor.BronzeCreditCardOffer(self)
        print("Cashback is : %s"%cashback)

class SilverCreditCard(CreditCard):
    def name(self):
        return "SilverCreditCard"

    def accept(self, visitor):
        cashback = visitor.SilverCreditCarOffer(self)
        print("Cashback is : %s"%cashback)

class GoldCreditCard(CreditCard):
    def name(self):
        return "GoldCreditCard"

    def accept(self, visitor):
        cashback = visitor.GoldCreditCardOffer(self)
        print("Cashback is : %s"%cashback)

class OfferVisitor(ABC):
    def BronzeCreditCardOffer(self, element):
        pass

    def SilverCreditCarOffer(self, element):
        pass

    def GoldCreditCardOffer(self, element):
        pass
        
class FoodOfferVisitor(OfferVisitor):
    def BronzeCreditCardOffer(self, element):
        print("BronzeCard food offfer.")
        return 5

    def SilverCreditCarOffer(self, element):
        print("SilverCard food offfer.")
        return 10

    def GoldCreditCardOffer(self, element):
        print("GoldCard food offfer.")
        return 20

class OtherOfferVisitor(OfferVisitor):
    def BronzeCreditCardOffer(self, element):
        print("BronzeCard other offer")
        return 2

    def SilverCreditCarOffer(self, element):
        print("SilverCard other offer")
        return 5

    def GoldCreditCardOffer(self, element):
        print("GoldCard other offer")
        return 10


visitor = FoodOfferVisitor()
cc = BronzeCreditCard()
cc.accept(visitor)

visitor = FoodOfferVisitor()
cc = GoldCreditCard()
cc.accept(visitor)

visitor = OtherOfferVisitor()
cc = GoldCreditCard()
cc.accept(visitor)