from collections import deque, defaultdict

class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = defaultdict(list)
        
    def connect(self, x, y):
        self.edges[x].append(y)
        self.edges[y].append(x)
    
    def find_all_distances(self, root):
        distances = [-1 for i in range(self.n)]
        unvisited = set([i for i in range(self.n)])
        q = deque()

        distances[root] = 0
        unvisited.remove(root)
        q.append(root)

        while len(q) != 0:
            node = q.popleft()
            height = distances[node]
            neighbors = self.edges[node]
            for n in neighbors:
                if n in unvisited:
                    distances[n] = height + 6
                    unvisited.remove(n)
                    q.append(n)

        distances.pop(root)

        print(" ".join(map(str, distances)))

t = input()
for i in range(t):
    n,m = [int(x) for x in raw_input().split()]
    graph = Graph(n)
    for i in xrange(m):
        x,y = [int(x) for x in raw_input().split()]
        graph.connect(x-1,y-1) 
    s = input()
    graph.find_all_distances(s-1)
