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

    def binaryCeil(self, arr, size, value):
        start = 0
        stop = size - 1        
        while start <= stop:
            mid = int((start + stop)//2)
            if (arr[mid] == value or (arr[mid] > value and (mid == 0 or arr[mid - 1] < value))):
                return mid
            elif (arr[mid] < value):
                start = mid + 1
            else:
                stop = mid - 1
        return len(arr)

    def searchCeil(self, arr, value):
        return self.binaryCeil(arr, len(arr), value)

    def addSorted(self, arr, value):
        index = self.binaryCeil(arr, len(arr), value)
        arr[index:index] = [value]

    def AddNode(self, id):
        for i in range(self.replicas):
            key = self.hash(id, i)
            if key in self.keys:
                continue
            self.nodes[key] = id
            #bisect.insort(self.keys, key)
            self.addSorted(self.keys, key)

    def RemoveNode(self, id):
        for i in range(self.replicas):
            key = self.hash(id, i)
            del self.nodes[key]
            #index = bisect.bisect_left(self.keys, key)
            index = self.searchCeil(self.keys, key)
            del self.keys[index]
            
    def GetNodeFromKey(self, value):
        key = self.hash(value, 0)
        start = bisect.bisect(self.keys, key)
        #start = self.searchCeil(self.keys, key)
        if start == len(self.keys):
            start = 0
        return self.nodes[self.keys[start]]


ch = ConsistentHash(20)
ch.AddNode("Server1")
ch.AddNode("Server2")
ch.AddNode("Server3")
ch.AddNode("Server4")

m = {}
for i in range(100000):
    server = ch.GetNodeFromKey(i)
    if server not in m:
        m[server] = 1
    else:
        m[server] += 1

for s in m:
    print("%s messages are sent to %s"%(m[s], s))
    
ch.RemoveNode("Server4")
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