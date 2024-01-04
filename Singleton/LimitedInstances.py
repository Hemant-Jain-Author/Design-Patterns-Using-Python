

class LimitedInstances(object):
    _instances = []  # Keep track of instance reference
    limit = 4 
 
    def __new__(cls):
        if not len(cls._instances) <= cls.limit:
            raise RuntimeError("Instance Limit reached")    
        instance = object.__new__(cls)
        cls._instances.append(instance)
        return instance
    
    def __del__(self):
        # Remove instance from _instances 
        self._instances.remove(self)

    
# Client code. 
LimitedInstances()
LimitedInstances()
LimitedInstances() 
LimitedInstances()
LimitedInstances() 
LimitedInstances()
LimitedInstances()
LimitedInstances() 
LimitedInstances()
LimitedInstances() 