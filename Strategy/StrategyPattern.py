from abc import ABC, abstractmethod

class Sorting(ABC):
    @abstractmethod
    def sort(self, numbers):
        pass

class BubbleSort(Sorting):
    def sort(self, numbers):
        # Bubble Sort Algorithm
        print("Bubble Sort Algorithm")        
        return numbers

class QuickSort(Sorting):
    def sort(self, numbers):
        # Quick Sort Algorithm
        print("Quick Sort Algorithm")
        return numbers

class StrategyClass:
    def __init__(self, algo = BubbleSort()):
        self.sorter = algo

    def setSorter(self, algo):
        self.sorter = algo
    
    def sort(self, a):
        a = self.sorter.sort(a)
        return a

a = []
for i in range(100):
    a.append(i)
s = StrategyClass()
print(s.sort(a))

s.setSorter(QuickSort())
print(s.sort(a))