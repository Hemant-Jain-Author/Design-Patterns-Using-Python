from abc import ABC, abstractmethod

class Agent: 
    def __init__(self):
        self._commands = []

    def placeOrder(self, command):
        self._commands.append(command)
        command.execute()

class ICommandOrder(ABC): 
    @abstractmethod
    def execute(self):
        pass

class BuyStockOrder(ICommandOrder):
    def __init__(self, stock):
        self.stock = stock
    
    def execute(self):
        self.stock.buy()

class SellStockOrder(ICommandOrder):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()

class ReceiverStockTrade:
    def buy(self):
        print("Buy stocks")
    
    def sell(self):
        print("Sell stocks")


stock = ReceiverStockTrade()
buyStock = BuyStockOrder(stock)
sellStock = SellStockOrder(stock)
agent = Agent()
agent.placeOrder(buyStock)
agent.placeOrder(sellStock)