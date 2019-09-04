class A(object):  
    def __init__(self):
        print("A created")

    def fun1(self): # member function
        print("fun1")
    
    def __del__(self): 
        print('A destroyed') 


class B(object):
    def __init__(self): #constructor
        print("B created")

    def fun2(self):
        print("fun2 start")
        A().fun1()
        print("fun2 end")
    
    def __del__(self): 
        print('B destroyed') 

c = B()
c.fun2()