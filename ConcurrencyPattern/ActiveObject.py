from queue import Queue
from threading import Thread
import time


# MethodRequest encapsulates a method call along with its arguments
class MethodRequest:
    def __init__(self, method, args):
        self.method = method
        self.args = args

    def execute(self):
        self.method(*self.args)


# ActiveObject encapsulates its own thread of control and executes methods asynchronously
class ActiveObject(Thread):
    def __init__(self):
        super().__init__()
        self.queue = Queue()
        self.is_running = True

    def run(self):
        while self.is_running or not self.queue.empty():
            method_request = self.queue.get()
            method_request.execute()

    def schedule_method(self, method, *args):
        method_request = MethodRequest(method, args)
        self.queue.put(method_request)

    def stop(self):
        self.is_running = False
        self.join()


# Proxy acts as a wrapper around the ActiveObject and forwards method calls to it
class Proxy:
    def __init__(self, active_object):
        self.active_object = active_object

    def invoke_method(self, method, *args):
        self.active_object.schedule_method(method, *args)


# Example usage
def print_message(message):
    print(message)

# Create an instance of ActiveObject and Proxy
active_object = ActiveObject()
proxy = Proxy(active_object)

# Start the ActiveObject thread
active_object.start()

# Invoke methods on the Proxy
proxy.invoke_method(print_message, "Hello")
proxy.invoke_method(print_message, "World")

# Stop the ActiveObject thread
active_object.stop()
