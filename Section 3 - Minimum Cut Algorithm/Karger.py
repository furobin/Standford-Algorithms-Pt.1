import random
import re
import numpy as np
from copy import deepcopy

file = open(r'C:\Users\foobe\Documents\Algorithms\Part 1\Section 3\Inputs.txt')
lines = file.readlines()
file.close()

lines = map(lambda s: re.sub('\s',' ',s).strip(),lines)
lines = map(lambda s: s.split(' '),lines)

verts = {}

for line in lines:
    verts[int(line[0])] = list(map(lambda s: int(s), line[1:]))
    
#%%
def distinctEdges(verts):
    edges = []
    vertCopy = deepcopy(verts)
    for k, v in vertCopy.items():
        #print(k,v)        
        while len(v) > 0:
            adj = v.pop()
            edges.append((k, adj))
            vertCopy[adj].remove(k)
    return edges

edges = distinctEdges(verts)
#%%
class Graph:
    '''
    Representation of Graph Data Type
    
    Parameters
    ----------
    verts : dict

    Attributes
    -------
    verts: dict{vert:edges}
    edges: tuple{v1, v2}
    
    '''
        
    def __init__(self, verts):
        self.verts = deepcopy(verts)
        self.edges = distinctEdges(self.verts)
        
    def contract(self, edge = None):
        if edge == None:
            edge = random.choice(self.edges)
        self.edges.remove(edge)
        #print(edge)
        v1 = min(edge)
        v2 = max(edge)
        self.verts[v1] = [edge for vert in [v1, v2]
                               for edge in self.verts[vert]
                               if edge not in [v1, v2]]
        self.verts.pop(v2)
        
        for v in self.verts.keys():
            for val in self.verts[v]:
                if v2 in self.verts[v]:
                    self.verts[v].remove(v2)
                    self.verts[v].append(v1)
                    try:
                        self.edges.remove((v2,v))
                        #print("removed", (v2,v))
                    except:
                        self.edges.remove((v,v2))
                        #print("removed", (v,v2))
                    
                    self.edges.append((v,v1))
                    #print(v2, "changed in v:", v)
        #print(self.edges)
        self.edges = [edge for edge in self.edges if edge[0] != v2 and edge[1] != v2]
        #print(self.edges)
                
        #PROBLEM: remove() deletes only one instance but may be multiple. use filter
        #Max # parallels per v is contractions + 1

g = Graph(verts)

#%%
def minCuts(verts):
    n = 5
    minCuts = float('inf')
    for i in range(1, int(n) + 1):
        print('Iteration: ', i)
        g = Graph(verts)
        while len(g.verts) > 2:
            g.contract()
        if len(g.edges) < minCuts:
            minCuts = len(g.edges)
    print(minCuts)
    return minCuts
            
minCuts(verts)
    

#%% Testing
v = {1 : [2,4,5],
     2 : [1,3,4],
     3 : [2,4,5],
     4 : [1,2,3,5],
     5 : [1,3,4]}

tg = Graph(v)


#%% Trash

class Vert:
    def __init__(self, ID, edges = []):
        self.ID = ID
        self.edges = edges
    
    @classmethod
    def contraction(cls, vert1, vert2):
        edges = [edge for vert in [vert1, vert2]
                      for edge in vert.edges
                      if edge not in [vert1.id, vert2.id]]
        return cls(min([vert1.id, vert2.id]), edges)
    
    def __eq__(self, other):
        return self.ID == other.ID
    
    def __lt__(self, other):
        return self.ID < other.ID
    
class Edge:
    def __init__(self, verts):
        self.verts = verts 
        
    def __eq__(self, other):
        return sorted(self.verts) == sorted(other.verts)
    
    def __repr__(self):
        return f'{self.verts[0]}, {self.verts[1]} |'