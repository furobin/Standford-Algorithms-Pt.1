"""
Strongly Connected Component (SCC) Search
"""

#This motherfucker is incorrect tho lmfao 

f = open(r'C:\Users\foobe\Documents\Algorithms\Part 1\Section 4\SCC.txt')
N = 875714
graph = []
graph_r = []
for i in range(N):
    graph += [[]]
    graph_r += [[]]
ls = f.readline()
while ls:
    data = list(map(int, ls.split(' ')[:-1]))
    ls = f.readline()
    if data[0] == data[1]:
        continue
    graph[data[0]-1] += [data[1]]
    graph_r[data[1]-1] += [data[0]]
f.close()

#%%

def create(g):
    return [i.copy() for i in g]


g1 = create(graph)
g2 = create(graph_r)

#%%

def DFS(g, i):
    global t, s, ex, f, leader, N #Creating global variables
    i -= 1 #Changing vert to match list indices
    ex[i] = True #Creating entry for explored entry
    leader[i] = s #Setting leader for this node to be s
    if len(g[i]) > 1: #As long as not =1
        for j in g[i][1:]: #Skips first one? Confuse
            if not ex[j-1]: #If not explored already, looks to see if in ex list
                DFS(g, j)
    t += 1 #increment t
    f[i] = t #set f value of node i
    print('V %i t= %i' % (i+1, t))


m = 0


def record(i): #Keeps record of t times found by 100ks
    global t, m
    if t >= m*100000:
        print('Point %i t=%i' % (i+1, t))
        m += 1


def tdone(g, i): #Effectively the DFS; never runs DFS function itself
    global f, t, leader, s, ex
    i -= 1 #setting node to index
    for j in g[i]: #For adjacents
        if not ex[j-1]: #If not explored already, matching j to index
            ex[j-1] = True #Set it to explored
            leader[j-1] = s #set leader to s
            return j #return self 
    t += 1 #increment t
    f[i] = t #Set fin time of i
    record(i) 
    return 0 #Only happens after having explored all j in g[i], that is, all edges from i. Backtracks


def DFS_loop(g):
    global t, s, ex, f, N
    for i in list(range(N))[::-1]: #iterating backwards over whole thing
        if not ex[i]: #If node unexplored 
            s = i+1 #Set leader to match node name, not index
            ex[i] = True #Mark node as explored
            leader[i] = s #Set leader of node as s
            exlist = [i+1] #Explored list? idk 
            while True:
                if len(exlist) == 0: #break when exlist empty
                    break
                j = tdone(g, exlist[-1]) #DFS func, uses last element of exlist
                #For first one, will use i above
                if j == 0:
                    exlist.pop(-1) #removes last element of exlist. Basically backtracks
                else: #happens when tdone returns during for statement
                    exlist += [j] #Looks to explore nodes extending from j, added to end of exlist


t = 0 #Fin time counter
s = None #Leader var
ex = [False]*N #Keeps track of explored
f = [0]*N #Keeps track of finish times
leader = [0]*N #Keeps track of leaders
print('Loop 1')
DFS_loop(g2)

#%%
for i in range(len(g1)):
    for j in range(len(g1[i])):
        g1[i][j] = f[g1[i][j]-1]
#Changes order of nodes for g1?
#%%
#Resetting global values 
t = 0
ex = [False]*N
f = [0]*N
leader = [0]*N
print('Loop 2')
m = 0
DFS_loop(g1)

sccdic = {}
for i in leader:
    if i in sccdic:
        sccdic[i] += 1
    else:
        sccdic[i] = 1

sccrank = list(sccdic.values())
sccrank.sort(reverse=True)
print(sccrank[:5])