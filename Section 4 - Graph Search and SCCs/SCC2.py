#%%
import copy
import time

#%% Test File
file = r'C:\Users\foobe\Documents\Algorithms\Part 1\Section 4\3-3-1-1-0.txt'

#%% RAID BOSS
file = r'C:\Users\foobe\Documents\Algorithms\Part 1\Section 4\SCC.txt'

#%%Loading File into graph
t1 = time.time()
graph = {}

with open(file, 'r') as f:
    for line in f.readlines():
        node, out = (int(i) for i in line.split(' ', 1))
        if node not in graph:
            graph[node] = Vert(node, heads = [out])
        else:
            graph[node].heads.append(out)
        if out not in graph:
            graph[out] = Vert(out, tails = [node])
        else:
            graph[out].tails.append(node)
            
t2 = time.time()

print("Elapsed: ", t2-t1)

#%% Vert Class
class Vert:
    '''
    Properties:
    
        ID: ID Number
        edges: IDs of adjacent nodes that are heads of this node
        
    '''
    
    def __init__(self, ID, heads = [], tails = []):
        self.ID = ID
        self.heads = heads.copy()
        self.tails = tails.copy()
        self.copy = None
        self.exp = False #explored boolean
        self.fin = 0 #finishing time
        self.leader = None #leader
    
    def __eq__(self, other):
        if type(other) == Vert:
            return self.ID == other.ID
        else:
            return self.ID == other
    
    def __hash__(self):
        return self.ID
    
#%% GPrint Func
def GPrint(graph):
    for i in graph:
        print(i, "Explored:", graph[i].exp, "Heads:", graph[i].heads, 
              "Tails:", graph[i].tails, "Leader:", graph[i].leader)
        
#%%
def ResetGraph(graph):
    '''
    Resetting exp parameter for vertices in graph

    Parameters
    ----------
    graph

    Returns
    -------
    None.

    '''
    for v in graph:
        graph[v].exp =False
        graph[v].leader = None
        
#%% Main Algorithm 
def DFSLoop(Graph):
    SCCSizes = []
    global t, s, finList
    t = 0
    s = None
    finList = []
    for v in Graph:
        if Graph[v].exp == False:
            s = Graph[v].ID
            DFS(Graph, Graph[v], Rev = True)
    print("Resetting Graph")
    ResetGraph(Graph)
    GPrint(Graph)
    while len(finList) != 0:
        v = finList.pop()
        if Graph[v].exp == False:
            s = Graph[v].ID
            DFS(Graph, Graph[v], Rev = False)
            
            
#%%
def DFS(Graph, v, Rev = False):
    explored = 0
    stack = [v]
    v.exp = True
    v.leader = s
    global counter
    counter = 0
    print("Current: ", v.ID)
    if Rev == False:
        for head in v.heads:
            if Graph[head].exp == False:
                print("trying :", head)
                DFS(Graph, Graph[head], Rev)
            else: 
                print("visited already")
                #counter += 1
            #if counter == 100:
                #break
    else:
        for tail in v.tails:
            if Graph[tail].exp == False:
                print("trying:", tail)
                DFS(Graph, Graph[tail], Rev = True)
            else:
                print("visited already")
                counter += 1
            #if counter == 100:
                #Cbreak
        finList.append(v.ID)
        
#%% #Regular DFS
def DFS(Graph, v):
    explored = 0
    stack = [v]
    v.exp = True
    while stack:
        v = stack.pop()
        print("popped")
        for edge in v.heads:
            if Graph[edge].exp == False:
                print(edge)
                Graph[edge].exp = True
                stack.append(Graph[edge])
                