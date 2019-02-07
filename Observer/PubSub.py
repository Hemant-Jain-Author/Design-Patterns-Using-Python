


class Broker(object):
    def __init__(self):
        self.subscribers = {}
 
    def subscribe(self, subs, topic):
        if topic in self.subscribers:
            self.subscribers[topic].append(subs)    
        else :
            self.subscribers[topic] = [subs]

        print('Subscribing: %s to topic: %s ' % (subs.id, topic))
 
    def notify(self, data, topic):
        if topic not in self.subscribers:
            return
 
        print('Publishing: %s in topic: %s ' %(data, topic))
        for subscriber in self.subscribers[topic]:
            subscriber.update(data)



class Subscriber(object):
    def __init__(self, id):
        self.id = id
 
    def update(self, data):
        print('Subscriber %s got :: %s'%(self.id, data))


if __name__ == '__main__':
    broker = Broker()
 
    sub1 = Subscriber('Subscriber1')
    sub2 = Subscriber('Subscriber2')
    print()
    broker.subscribe(sub1, 'topic1')
    broker.subscribe(sub2, 'topic2')
    print()
    broker.notify('Topic 1 data', 'topic1')
    broker.notify('Topic 2 data', 'topic2')