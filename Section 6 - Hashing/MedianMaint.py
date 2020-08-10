#%%
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

import Heap #own heaps 
#%% Reading numbers from file via generator
file = r'C:\Users\foobe\Documents\Algorithms\Part 1\Section 6\median.txt'

def number_gen(file):
    with open(file, 'r') as f:
        for line in f.readlines():
            yield int(line)

#%%
import Heap

#%%
def MedianMaint(file):
    Smalls = Heap.MaxHeap()
    Bigs = Heap.MinHeap()
    numbers = number_gen(file)
    start = (next(numbers), next(numbers)) #First two values
    Smalls.Insert(min(start))
    print(Smalls.data)
    Bigs.Insert(max(start))
    print(Bigs.data)
    total = start[0] + min(start)
    k = 2 #number of elements seen so far
    while True:
        try:
            new = next(numbers)
            if new > Bigs.data[0]: #The min of large elements
                Bigs.Insert(new)
            else: #nnew <= Smalls.data[0], largest of small elements
                Smalls.Insert(new)
            if len(Bigs.data) > len(Smalls.data):
                Smalls.Insert(Bigs.ExtractMin()) #If Big > Small by 1, take Min from Big and put in Smalls
                #Ensures Smalls >= Bigs
            elif len(Smalls.data) > len(Bigs.data) + 1: #If Small bigger than Bigs by 2
                Bigs.Insert(Smalls.ExtractMax())
            total += Smalls.data[0]
        except StopIteration:
            print("Numbers exhausted")
            break
    print(len(Smalls.data))
    print(len(Bigs.data))
    return total % 10000
    

#Correct Answer: 1213