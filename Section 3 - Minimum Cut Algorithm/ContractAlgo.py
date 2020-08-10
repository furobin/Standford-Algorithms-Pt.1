import random
import re
from copy import deepcopy

file = open('Inputs.txt')
lines = file.readlines()
file.close()

lines = map(lambda s: re.sub('\s',' ',s).strip(),lines)
lines = map(lambda s: s.split(' '),lines)



verts = []

for line in lines:
    verts.append(Vert(line[0],line[1:]))
    
#%%
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
        
class Graph:
    def __init__(self, verts):
        self.verts = dict((v.ID, v) for v in verts)
        
    @property
    def edges(self):
        edges = list([Edge((vert.ID, e)) for vert in self.verts.values() for e in vert.edges ])
        return edges
    
        
        
v1 = Vert(1, [2,3,4])
v2 = Vert(2, [1])
v3 = Vert(3, [1])
v4 = Vert(4, [1])
vertlist = [v1,v2,v3,v4]
graph1 = Graph(vertlist)

g = Graph(verts)
