class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []

    def peek(self):
        if len(self.second) != 0:
            return self.second[len(self.second) - 1]
        else:
            if len(self.first) != 0:
                return self.first[0]
            else:
                return None
 
    def pop(self):
        if len(self.second) != 0:
            return self.second.pop()
        else:
            if len(self.first) != 0:
                while len(self.first):
                    item = self.first.pop()
                    self.second.append(item)
                return self.second.pop()
            else:
                return None

    def put(self, value):
        self.first.append(value)

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
