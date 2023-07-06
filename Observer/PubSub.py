class Publisher(object):
    def __init__(self):
        self.topic_subscribers = {}
 
    def subscribe(self, subs, topic):
        if topic in self.topic_subscribers:
            self.topic_subscribers[topic].append(subs)    
        else :
            self.topic_subscribers[topic] = [subs]

        print('Subscribing: %s to topic: %s ' % (subs.id, topic))


    def unsubscribe(self, subs, topic):
        if topic in self.topic_subscribers:
            self.topic_subscribers[topic].remove(subs)    

        print('UnSubscribing: %s to topic: %s ' % (subs.id, topic))

 
    def notify(self, data, topic):
        if topic not in self.topic_subscribers:
            return
 
        print('Publishing: %s in topic: %s ' %(data, topic))
        for subscriber in self.topic_subscribers[topic]:
            subscriber.update(data)


class Subscriber(object):
    def __init__(self, id):
        self.id = id
 
    def update(self, data):
        print('Subscriber %s got :: %s'%(self.id, data))


# Client code
pub = Publisher()
 
sub1 = Subscriber('Subscriber1')
sub2 = Subscriber('Subscriber2')
sub3 = Subscriber('Subscriber3')

print()
pub.subscribe(sub1, 'topic1')
pub.subscribe(sub2, 'topic2')
pub.subscribe(sub3, 'topic2')

print()
pub.notify('Topic 1 data', 'topic1')

print()
pub.notify('Topic 2 data', 'topic2')

print()
pub.unsubscribe(sub3, 'topic2')
pub.notify('Topic 2 data', 'topic2')

"""
Subscribing: Subscriber1 to topic: topic1 
Subscribing: Subscriber2 to topic: topic2 
Subscribing: Subscriber3 to topic: topic2 

Publishing: Topic 1 data in topic: topic1 
Subscriber Subscriber1 got :: Topic 1 data

Publishing: Topic 2 data in topic: topic2 
Subscriber Subscriber2 got :: Topic 2 data
Subscriber Subscriber3 got :: Topic 2 data

UnSubscribing: Subscriber3 to topic: topic2 
Publishing: Topic 2 data in topic: topic2 
Subscriber Subscriber2 got :: Topic 2 data

"""    


