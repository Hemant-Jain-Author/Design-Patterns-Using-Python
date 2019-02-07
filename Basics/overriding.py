class A:
    def operation(self):
        print("operation method from class A")
 
class B(A):
    def operation(self):
        super().operation()  # calling the parent class operation method
        print("operation method from class B")
 
 
b = B()
b.operation()