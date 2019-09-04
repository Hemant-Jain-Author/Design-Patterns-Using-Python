class Publisher(object):
    def __init__(self):
        self.topicSubscribers = {}
 
    def subscribe(self, subs, topic):
        if topic in self.topicSubscribers:
            self.topicSubscribers[topic].append(subs)    
        else :
            self.topicSubscribers[topic] = [subs]

        print('Subscribing: %s to topic: %s ' % (subs.id, topic))


    def unSubscribe(self, subs, topic):
        if topic in self.topicSubscribers:
            self.topicSubscribers[topic].remove(subs)    

        print('UnSubscribing: %s to topic: %s ' % (subs.id, topic))

 
    def notify(self, data, topic):
        if topic not in self.topicSubscribers:
            return
 
        print('Publishing: %s in topic: %s ' %(data, topic))
        for subscriber in self.topicSubscribers[topic]:
            subscriber.update(data)


class Subscriber(object):
    def __init__(self, id):
        self.id = id
 
    def update(self, data):
        print('Subscriber %s got :: %s'%(self.id, data))


if __name__ == '__main__':
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
    pub.unSubscribe(sub3, 'topic2')
    pub.notify('Topic 2 data', 'topic2')

    