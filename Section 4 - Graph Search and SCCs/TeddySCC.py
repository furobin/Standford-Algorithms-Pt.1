############
# Standard #
############
import copy
import logging

############
# External #
############

###########
# Package #
###########

logger = logging.getLogger(__name__)

class Node:
    """
    Node in a Graph
    Parameters
    ----------
    _id : int
        Integer id of the node
    incoming : list of int
         Nodes that have directed edges arriving at this node
    outgoing : list of int
         Nodes that have directed edges originating from this node
    Attributes
    ----------
    explored : bool
        Whether the node has been seen by the current algorithm
    leader : int
        Local variable to use in depth_search
    """
    def __init__(self, _id, edges=None):
        self.id = _id
        self.edges = edges or list() #negative edges are incoming, positive are outgoing 
        self.explored = False
        self.finished = False

    def __repr__(self):
        return '<Node {}, connected to {}>'.format(self.id, self.edges)
    
    #This structure pretty similar to my own, likely difference is in DFS


class Graph:
    """
    Graph Structure
    Parameters
    ----------
    nodes : Node
        Nodes in graph
    """
    def __init__(self):
        self.nodes = dict()

    @classmethod
    def from_adjacency_list(cls, path):
        """
        Load the network from an adjacency list
        """
        obj = cls()
        # Read the node information from file
        with open(path, 'r') as f:
            for line in f.readlines():
                (_id, out) = (int(i) for i in line.split(' ', 1))
                # Add the node to the graph
                if _id not in obj.nodes:
                    obj.nodes[_id] = Node(_id, edges=[out])
                else:
                    obj.nodes[_id].edges.append(out)
                #Add to the edge of the obj
                if out not in obj.nodes:
                    obj.nodes[out] = Node(out, edges=[-_id])
                else:
                    obj.nodes[out].edges.append(-_id)
        return obj

    def reverse(self):
        """
        Reverse the graph edges
        """
        for node in self.nodes.values():
            node.edges = [-edge for edge in node.edges]
            node.explored = False
            node.finished = False
            
    #Also fairly similar to mine; my graph is also a dictionary. Reverse just uses tail and head

def find_scc(adj_list):
    """
    Find all the strongly connnected components in a graph
    Parameters
    ----------
    graph : Graph
    Returns
    -------
    scc : list
        List of scc sizes
    """
    def depth_first_search(node):
        explored = 0
        # Keep a stack of nodes to search through
        stack = [node]
        # Keep traversing the graph 
        while stack: #while stack not empty
            node = stack[-1] #observe last element
            if node.explored: #if node is explored, this section wraps it up
                # Record the finishing time of the node by placing it in
                # the correct place in our finishing time array 
                if not node.finished:
                    node.finished = True
                    f.append(stack.pop()) #same as my finList, once node finished, added to f.append from back. Last finish = last element
                # Make sure we do not double add a previously finished node.
                # This is possible if a node is added to the stack but is then
                # added to the finished list by a higher priority dfs
                else: 
                    stack.pop() #Note, if all nodes cannot go anywhere, stack will pop itself empty
            else:
                # Mark the node as explored and add it to the tally
                node.explored = True #sets node to explored
                explored += 1 #increses # explreod nodes by one
                # For each possible step from this node, if we haven't already
                # explored the destination node. Then make a recursive call
                for edge in node.edges: #checks all edges from this node; if edge is outgoing, it is positive
                    if edge > 0  and not graph.nodes[edge].explored: #makes sure node at edge not explroed
                        stack.append(graph.nodes[edge]) #appends to stack, will be hecked next 
        return explored #Total number of nodes found FROM this node. I GET IT NOW. VERY COOL. MUCH BETTERH THAN MINE. AN DUMB. 

    def depth_loop(node_order):
        f.clear() #clears finished list
        components = list()
        # For each of our nodes, if we haven't already explored it, start a
        # depth first search from here. Store the information on the size of
        # the component
        for node_id in node_order:
            # Grab the node information from our graph
            node = graph.nodes[node_id.id]
            if not node.explored:
                logger.info("Starting new depth first search at %s", node)
                # Add the size of the depth first search
                components.append(depth_first_search(node))
                logger.info("Found component of size %s", components[-1])
        return components #List of number of nodes found from each node when DFS initiated.

    # Run the depth_loop on the reversed graph
    # to discover the fine structure
    logger.info("Loading the graph from file ...")
    graph = Graph.from_adjacency_list(adj_list)
    logger.debug("Reversing the graph for the first depth loop run")
    graph.reverse()
    # Create an array to store finishing times in
    f = list()
    depth_loop(sorted(graph.nodes.values(),
                      key=lambda x : x.id,
                      reverse=True)) #runs depth_loop on nodes, value high to low. Basically sorts nodes high to low, then runs
    finishing_times = list(reversed(copy.copy(f)))
    # Create a copy of the finish time list and using this, rerun the
    # depth_loop on the regular graph to find all the strongly connected
    # components
    logger.debug("Reversing the graph again... ")
    graph.reverse()
    logger.info("Running depth first search again with finish time order")
    components = depth_loop(finishing_times)
    # Return the Top 5 most populated components, padding with zeros in the
    # event that there are not five strongly correlated components
    components.extend([0]*5) #adds 5 zero elements to end of list lmao
    return sorted(components, reverse=True)[:5] #sorted creates copy, list.sort() works in place on self

#%%
final = find_scc(r'C:\Users\foobe\Documents\Algorithms\Part 1\Section 4\SCC.txt')
print(final)

#%%
graph = Graph.from_adjacency_list(r'C:\Users\foobe\Documents\Algorithms\Part 1\Section 4\3-3-1-1-0.txt')

#%%
import time

t1 = time.time()
other = Graph.from_adjacency_list(r'C:\Users\foobe\Documents\Algorithms\Part 1\Section 4\SCC.txt')
t2 = time.time()
print("Elapsed: ",t2 - t1)