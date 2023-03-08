class MatrixGraph:
    graph = []
    size = 0
    node = []
    weight = []

    def __init__(self,elements):
        self.size = len(elements)
        self.node = elements
        for i in range (self.size + 1):
            row = []
            for j in range(self.size + 1):
                row.append('0')
            self.graph.append(row)

        for k in range(0, self.size):
            self.graph[k+1][0] = self.node[k]
            self.graph[0][k+1] = self.node[k]


        for m in range(0,self.size):
            self.weight.append(1)

    def Print(self):
        for i in range (self.size+1):
            for j in range(self.size+1):
                print("| " +self.graph[i][j] + " " , end='')
            print("|")

    def AddVertex(self,a,b):
        p1 = self.node.index(a) + 1
        p2 = self.node.index(b) + 1
        self.graph[p1][p2] = "1"

    def AddBiconnectedVertex(self,a,b):
        p1 = self.node.index(a) + 1
        p2 = self.node.index(b) + 1
        self.graph[p1][p2] = "1"
        self.graph[p2][p1] = "1"

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
            x = self.node.index(v) + 1

            l =  len(self.node) + 1

            for i in range(l):
                if (self.graph[x][i] == "1"):
                    if (isVisited[i-1] == "F"):
                        L.append([v,self.node[i-1]])
                        print(self.node[i-1])
                        queue.append(self.node[i-1])
                        isVisited[i-1] = "T"

        return L

    def DFS(self,n):
        print(n)
        queue = []
        L = []
        isVisited = ["F","F","F","F","F","F","F"]

        queue.append(n)

        pos = self.node.index(n)

        isVisited[pos] = "T"

        while (len(queue) > 0):
            v = queue.pop(0)
            x = self.node.index(v) + 1

            l =  len(self.node) + 1

            for i in range(l):
                if (self.graph[x][i] == "1"):
                    if (isVisited[i-1] == "F"):
                        L.append([v,self.node[i-1]])
                        print(self.node[i-1])
                        queue.append(self.node[i-1])
                        isVisited[i-1] = "T"

        return L

    def RemoveVertex(self,a,b):
        p1 = self.node.index(a) + 1
        p2 = self.node.index(b) + 1
        self.graph[p1][p2] = "0"

    def AddWeigthedVertex(self,a,b,w):
        p1 = self.node.index(a) + 1
        p2 = self.node.index(b) + 1
        self.graph[p1][p2] = "1"
        self.weight = w

    def FindWeightedVertex(self,n):
        Vertex = []
        x = self.node.index(n) + 1
        row = self.graph[x]
        for i in range(0,len(row)):
            if (row[i] == "1"):
                Vertex.append([self.node[i-1],self.weight[i-1]])
                print(self.node[i-1])
        return Vertex

    def FindVertex(self,n):
        Vertex = []
        x = self.node.index(n) + 1
        row = self.graph[x]
        for i in range(0,len(row)):
            if (row[i] == "1"):
                Vertex.append(self.node[i-1])
                print(self.node[i-1])
        return Vertex

    def FindPath(self,a,b):
        isVisited = ["F","F","F","F","F","F","F"]
        # Create a stack
        stack = []
        # Push a into the stack
        stack.append(a)
        # mark a as visited
        while (len(stack) >= 0):
            head = stack[0]
            print(head)
            if (head == b):
                result = []
                for s in stack:
                    sidx = self.node.index(s)
                    print(isVisited[sidx])
                    if (isVisited[sidx] == "T"):
                        result.append(s)
                result.insert(0,b)
                result.reverse()
                return result
            idx = self.node.index(head)
            isVisited[idx] = "T"
        # look for all the neighbors of a that is not visited
            neighbor = self.FindVertex(head)
            tmpNeighbor = []
            for n in neighbor:
                nidx = self.node.index(n)
                if (isVisited[nidx] == "F"):
                    tmpNeighbor.append(n)
            neighbor = tmpNeighbor
            # print(len(neighbor))
        # If there is a has no neighbor pop until we reach the head of the stack that is still not visible
            if (len(neighbor) == 0):
                while(isVisited[self.node.index(stack[0])] == "T"):
                    stack.pop(0)
        # Else push all the neighbors of a into the stack
            else:
                print("asda")
                for v in neighbor:
                    stack.insert(0,v)



        return stack

