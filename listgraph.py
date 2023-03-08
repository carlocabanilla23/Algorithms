class ListGraph:
    graph = []
    size = 0
    node = []
    weight = []
    
    def __init__(self,elements):
        self.size = len(elements)
        self.node = elements
        for i in elements:
            row = [i]
            self.graph.append(row)
            row = []
        
    def Print(self):
        for v in self.graph:
            print(v) 
            
    def AddVertex(self,a,b):
        vPos = self.node.index(a)
        self.graph[vPos].append(b)

    def AddBiconnectedVertex(self,a,b):
        vPosA = self.node.index(a)
        vPosB = self.node.index(b)

        self.graph[vPosA].append(b)
        self.graph[vPosB].append(a)

    def BFS(self,n):
        print(n)
        queue = []
        L = []
        isVisited = ["F","F","F","F","F","F","F"]

        queue.append(n)

        pos = self.node.index(n)

        isVisited[pos] = "T"

        while (len(queue) > 0):
            v = queue.pop()
            x = self.node.index(v)
            isVisited[x] = "T"
            l =  len(self.graph[x])
            # print(self.graph[x])
            # print(l)
            for n in self.graph[x]:
                    pos = self.node.index(n)
                    if (isVisited[pos] == "F"):
                        L.append([v,self.node[pos]])
                        print(self.node[pos])
                        queue.append(self.node[pos])
                        isVisited[pos] = "T"

        return L