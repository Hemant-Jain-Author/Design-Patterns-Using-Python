class Model(object):
    def getData(self):
        data = 'Hello, World!'
        print("Model: Business logic applied and data returned:", data)
        return data

class View(object):
    def update(self, data):
        print("View: Updating the view with data: ", data)

class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()

    def interface(self):
        print("Controller: Receive trigger from client.")
        data = self.model.getData()
        self.view.update(data)

class Client(object):
    print("Client: Pass trigger to Controller.")
    controller = Controller()
    controller.interface()