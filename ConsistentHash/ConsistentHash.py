import bisect
import hashlib

class ConsistentHash:
    def __init__(self, rep):
        self.keys = []
        self.nodes = {}
        self.replicas = rep

    def hash(self, nodeid, rep):
        value = str(nodeid) + ":" + str(rep)
        hash_object = hashlib.md5(value.encode())
        return hash_object.hexdigest()

    def AddNode(self, id):
        for i in range(self.replicas):
            key = self.hash(id, i)
            if key in self.keys:
                continue
            self.nodes[key] = id
            bisect.insort(self.keys, key)

    def RemoveNode(self, id):
        for i in range(self.replicas):
            key = self.hash(id, i)
            del self.nodes[key]
            index = bisect.bisect_left(self.keys, key)
            del self.keys[index]
            
    def GetNodeFromKey(self, key):
        base = self.hash(key, 0)
        start = bisect.bisect(self.keys, base)
        if start == len(self.keys):
            start = 0
        return self.nodes[self.keys[start]]


ch = ConsistentHash(20)
ch.AddNode("Server1")
ch.AddNode("Server2")
ch.AddNode("Server3")
ch.AddNode("Server4")
ch.AddNode("Server5")
ch.AddNode("Server6")
ch.AddNode("Server7")
ch.AddNode("Server0")

m = {}

for i in range(100000):
    server = ch.GetNodeFromKey(i)
    if server not in m:
        m[server] = 1
    else:
        m[server] += 1


for s in m:
    print("%s messages are sent to %s"%(m[s], s))
    
ch.RemoveNode("Server0")
print()
m = {}
for i in range(100000):
    server = ch.GetNodeFromKey(i)
    if server not in m:
        m[server] = 1
    else:
        m[server] += 1


for s in m:
    print("%s messages are sent to %s"%(m[s], s))
