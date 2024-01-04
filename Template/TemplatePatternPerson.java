from abc import ABC, abstractmethod

class AbstractWorker(ABC):
    def dailyRoutine(self):   # Final method
        self.wakeUp()
        self.eatBreakfast()
        self.goToWork()
        self.work()
        self.comeBackHome()
        self.eatDinner()
        self.sleep()

    def wakeUp(self):
        print("Wake Up")
    
    def eatBreakfast(self):
        print("Eat Breakfast")
    
    def goToWork(self):
        print("Go to work")
    
    @abstractmethod
    def work(self):
        pass
    
    def comeBackHome(self):
        print("Come back Home")
    
    def eatDinner(self):
        print("Eat dinner")
    
    def sleep(self):
        print("Sleep")


class Doctor(AbstractWorker):
    def work(self):
        print("...Treat Patients...")

class FireFighter(AbstractWorker):
    def work(self):
        print("...Fight Fire...")

class SuperHero(AbstractWorker): 
    def work(self):
        print("...Save the world!...")

# Client Code 
d = Doctor()
d.dailyRoutine()
print()

f = FireFighter()
f.dailyRoutine()
print()

s = SuperHero()
s.dailyRoutine()

"""
Output:
Wake Up
Eat Breakfast
Go to work
...Treat Patients...
Come back Home
Eat dinner
Sleep

Wake Up
Eat Breakfast
Go to work
...Fight Fire...
Come back Home
Eat dinner
Sleep

Wake Up
Eat Breakfast
Go to work
...Save the world!...
Come back Home
Eat dinner
Sleep

"""

