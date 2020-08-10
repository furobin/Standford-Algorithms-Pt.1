#%%
import copy
import time

#%%
class Vert:
    '''
    Properties:
    
        ID: ID Number
        edges: IDs of adjacent nodes that are heads of this node
        
    '''
    
    def __init__(self, ID, heads = [], dist = []):
        self.ID = ID
        self.heads = heads.copy()
        self.dist = dist.copy()
    
    def __eq__(self, other):
        if type(other) == Vert:
            return self.ID == other.ID
        else:
            return self.ID == other
    
#%%
def VPrint(Vert):
    print("ID: ", Vert.ID, "heads: ", Vert.heads, "Dists: ", Vert.dist)

#%% Loading the file
t1 = time.time()

file = r"C:\Users\foobe\Documents\Algorithms\Part 1\Section 5\djk.txt"

graph = {}

with open(file, 'r') as f:
    for line in f.readlines():
        Llist = line.split() #splitting each line into a list of its elements
        node = int(Llist.pop(0))
        graph[node] = Vert(node, [int(v.split(',')[0]) for v in Llist],
                                 [int(v.split(',')[1]) for v in Llist])

t2 = time.time()
print('Elapsed Time: ', t2-t1)

#%%
 
def Dijkstras(Graph, v):
    graph = copy.deepcopy(Graph) #Done here just for convenience
    A = {v.ID : 0} #Seen vertices and distances from source
    for node in graph.keys(): #Removes 1 as head from all other nodes
        if v.ID in graph[node].heads:
            pos = graph[node].heads.index(v.ID)
            graph[node].heads.pop(pos)
            graph[node].dist.pop(pos)
    loopcount = 0
    while len(A) != len(Graph) and loopcount <= 200:
        GC = {}
        for k in A.keys():
            #print("Looking at edges of node: ", k)
            for index in range(len(graph[k].heads)):
                head = graph[k].heads[index] #edge node from k which is in A
                #print("Looking at head: ", head)
                dist = graph[k].dist[index] #dist to edge from k
                score = A[k] + dist
                #print("Scored: ", score)
                if head not in GC:
                    GC[head] = score
                else:
                    if score < GC[head]:
                        GC[head] = score
        if loopcount == 200:
            print("loopcount Maxed")
        if len(GC) == 0:
            print("GC empty")
            return A, GC, graph
        added = min(GC, key = GC.get) #A node ID
        #print("Added node: ", added)
        A[added] = GC.pop(added)
        for node in graph.keys(): #Removes 1 as head from all other nodes
            if added in graph[node].heads:
                pos = graph[node].heads.index(added)
                graph[node].heads.pop(pos)
                graph[node].dist.pop(pos)
        loopcount += 1
    #print(loopcount)
    return A, GC, graph
    
                
    
#Correct answer for vertices 7, 37, 59, 82, 99, 115, 133, 165, 188, 197 is
#2599, 2610, 2947, 2052, 2367, 2399, 2029, 2442, 2505, 3068

#%%
def HeadCheck(A, graph):
    Count = 0
    for key in A.keys():
        for node in graph.values():
            if key in node.heads:
                print("You Fail")
                break
        print("Successfully deleted: ", key)
        Count += 1
    print("Checked ", Count)
    
    
#%%
t1 = time.time()

A, GC, NewGraph = Dijkstras(graph, graph[1])

t2 = time.time()

print("Elapsed: ", t2-t1)