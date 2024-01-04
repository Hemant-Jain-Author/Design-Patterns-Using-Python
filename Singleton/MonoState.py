class MonoState(object):
    __sharedState = {}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__sharedState


# Client code. 
m = MonoState()
m1 = MonoState()
print("MonoState Object 'm': ", m) # m and m1 are distinct objects
print("MonoState Object 'm1': ", m1)

m.x = 5
print("Object State 'm':", m.__dict__) # m and m1 share same state
print("Object State 'm1':", m1.__dict__)