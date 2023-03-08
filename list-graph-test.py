import listgraph as g

file = open('test.txt','r')
line = file.readlines()

elements = line[0].split(' ')

elements[len(elements)-1] = elements[len(elements)-1].strip()

x = g.ListGraph(elements)

for i in range(1,len(line)):
    nodes = line[i].split(' ')
    nodes[len(nodes)-1] = nodes[len(nodes)-1].strip()
    p1 = nodes[0]
    p2 = nodes[1]
    x.AddBiconnectedVertex(p1,p2)

x.Print()
print()
print()
print("BFS")
bfsResult = x.BFS("A")
print(bfsResult)