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
        
#%%
def BFS(graph, Vert):
    Vert.exp = True
    queue = [Vert]
    while queue:
        v = queue.pop(0)
        for edge in v.heads:
            if edge.explored == False:
                edge.explored = True
                queue.append(edge)