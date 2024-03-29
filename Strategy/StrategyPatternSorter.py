from abc import ABC, abstractmethod

class Sorting(ABC):
    @abstractmethod
    def sort(self, numbers):
        pass

class BubbleSort(Sorting):
    def sort(self, numbers):
        # Bubble Sort Algorithm
        print("Bubble Sort Algorithm executed.")        
        size = len(numbers)
        for i in range(size - 1):
            for j in range(size - i - 1):
                if numbers[j] > numbers[j + 1]:
                    #  Swapping 
                    temp = numbers[j]
                    numbers[j] = numbers[j + 1]
                    numbers[j + 1] = temp

class SelectionSort(Sorting):
    def sort(self, numbers):
        # Selection Sort Algorithm
        print("Selection Sort Algorithm executed.")
        # reverse array creation
        size = len(numbers)
        for i in range(size - 1):
            maxIndex = 0
            for j in range(1, size - i):
                if numbers[j] > numbers[maxIndex]:
                    maxIndex = j
            temp = numbers[size - 1 - i]
            numbers[size - 1 - i] = numbers[maxIndex]
            numbers[maxIndex] = temp



class StrategyClass:
    def __init__(self, algo = BubbleSort()):
        self.sorter = algo

    def set_sorter(self, algo):
        self.sorter = algo
    
    def sort(self, a):
        a = self.sorter.sort(a)
        return a

#Client code.
a = [4, 5, 3, 2, 6, 7, 1, 8, 9, 10]
s = StrategyClass()
s.sort(a)
print(a)

a = [4, 5, 3, 2, 6, 7, 1, 8, 9, 10]
s.set_sorter(SelectionSort())
s.sort(a)
print(a)

"""
Bubble Sort Algorithm executed.
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Selection Sort Algorithm executed.
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
