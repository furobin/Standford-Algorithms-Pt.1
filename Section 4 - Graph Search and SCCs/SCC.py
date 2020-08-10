import re
import numpy as np
from collections import defaultdict
import sys 

sys.setrecursionlimit(7500)

#%% Test File
file = open(r'C:\Users\foobe\Documents\Algorithms\Part 1\Section 4\3-3-1-1-0.txt')
lines = file.readlines()
file.close()

#%% Main File
file = open(r'C:\Users\foobe\Documents\Algorithms\Part 1\Section 4\SCC.txt')
lines = file.readlines()
file.close()

#%% Load file into lines object, list of lists
lines = map(lambda s: re.sub('\s',' ',s).strip(),lines)
lines = map(lambda s: s.split(' '),lines)
lines = list(lines)

#%%
#Finds number of nodes n assuming nodes numbered 1 to n
n = max(int(item) for sublist in lines for item in sublist) 

#%%
vertDict = {}
tailDict = {}

for i in range(1, n + 1):
    vertDict[i] = []
    tailDict[i] = []

for line in lines:
    vertDict[int(line[0])].append(int(line[1]))
    tailDict[int(line[1])].append(int(line[0]))
    
del lines, file
#%%
class Vert:
    '''
    Properties:
    
        ID: ID Number
        edges: IDs of adjacent nodes that are heads of this node
        
    '''
    
    def __init__(self, ID, heads = [], tails = []):
        self.ID = ID
        self.heads = heads
        self.tails = tails
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
    
#%% Timing Loading
import time
t1 = time.time()

file = open(r'C:\Users\foobe\Documents\Algorithms\Part 1\Section 4\SCC.txt')
lines = file.readlines()
file.close()

lines = map(lambda s: re.sub('\s',' ',s).strip(),lines)
lines = map(lambda s: s.split(' '),lines)
lines = list(lines)

t2 = time.time()

print("Elapsed: ", t2-t1)


n = max(int(item) for sublist in lines for item in sublist) 

vertDict = {}
tailDict = {}

for i in range(1, n + 1):
    vertDict[i] = []
    tailDict[i] = []

for line in lines:
    vertDict[int(line[0])].append(int(line[1]))
    tailDict[int(line[1])].append(int(line[0]))
    
del lines, file

t3 = time.time()

print("Elapsed: ", t3-t2)

graph = {}

for k,v in vertDict.items():
    graph[k] = Vert(k, v)
    
for k,v in tailDict.items():
    graph[k].tails = v
    
for v in graph:
    graph[v].copy = (graph[v].heads.copy(), graph[v].tails.copy())

del tailDict, vertDict

t4 = time.time()
print("Elapsed: ", t4-t3)

#%%
def GPrint(graph):
    for i in graph:
        print(i, "Explored:", graph[i].exp, "Heads:", graph[i].heads, 
              "Tails:", graph[i].tails, "Leader:", graph[i].leader)
#%% Main Algorithm
        
def DFSLoop(Graph):
    global t
    t = 0
    global s
    s = None
    global finList 
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
        graph[v].heads, graph[v].tails = graph[v].copy #This is actually not necessary lmao
#%% Testing DFS
#s = 1
#finList = []

def DFS(Graph, v, Rev = False):
    v.exp = True
    v.leader = s
    global counter
    counter = 0
    print("Current: ", v.ID)
    if Rev == False:
        heads = v.heads.copy()
        for others in Graph:
            if v in Graph[others].heads:
                Graph[others].heads.remove(v) #Remove all occurences of v in other heads
        for head in heads:
            if Graph[head].exp == False:
                print("trying :", head)
                DFS(Graph, Graph[head], Rev)
            else: 
                print("visited already")
                #counter += 1
            #if counter == 100:
                #break
    else:
        tails = v.tails.copy()
        for others in Graph:
            if v in Graph[others].tails:
                Graph[others].tails.remove(v) #Remove all occurences of v in other tails
        for tail in tails:
            if Graph[tail].exp == False:
                print("trying:", tail)
                DFS(Graph, Graph[tail], Rev = True)
            else:
                print("visited already")
                counter += 1
            #if counter == 100:
                #Cbreak
        finList.append(v.ID)

#%%
def CountSCCs(graph):
    '''
    Counting SCCs of a graph processed by DFSLoop

    Parameters
    ----------
    graph

    Returns
    -------
    None.

    '''
    SCC = defaultdict(int)
    for vert in graph:
        lead = graph[vert].leader
        SCC[lead] += 1
    results = list(SCC.values())
    results.sort(reverse = True)
    return results
    
#%%

DFSLoop(graph)

print(CountSCCs(graph))

#Correct Answer: 434821 968, 459, 313, 211
