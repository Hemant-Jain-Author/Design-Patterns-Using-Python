from abc import ABC, abstractmethod

class Agent: # invoker 
    def place_order(self, command):
        command.execute()

class Order(ABC): 
    @abstractmethod
    def execute(self):
        pass

class BuyStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock
    
    def execute(self):
        self.stock.buy()

class SellStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()

class ReceiverStockTrade:  # Receiver
    def buy(self):
        print("Buy stocks")
    
    def sell(self):
        print("Sell stocks")

# Client code.
trader = ReceiverStockTrade()
buyStock = BuyStockOrder(trader)
sellStock = SellStockOrder(trader)
agent = Agent()
agent.place_order(buyStock)
agent.place_order(sellStock)

"""
Buy stocks
Sell stocks
"""