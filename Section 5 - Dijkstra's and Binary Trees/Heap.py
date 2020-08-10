#%%
import math

#%%
class MinHeap:
    
    def __init__(self, data = []):
        self.data = data.copy()
    
    @classmethod
    def Heapify(cls, data = []):
        for root in range(len(data)//2-1, -1, -1):
            rootVal = data[root]
            child = root * 2 + 1
            while child < len(data):
                if child + 1 < len(data) and data[child] > data[child + 1]:
                    child +=1 #Finding minimum of 2 children
                if rootVal <= data[child]:
                    break
                data[child], data[(child-1)//2] = data[(child-1)//2], data[child]
                child = child * 2 + 1
        obj = cls(data)
        return obj
    
    def FindParent(self, index):
        assert index <= len(self.data) - 1, "Index out of range"
        parent = (index -1)//2
        return self.data[parent]
        
    def FindChild(self, index):
        child = index * 2 + 1
        if child + 1 <= len(self.data) - 1:
            return (self.data[child], self.data[child + 1])
        elif child == len(self.data) - 1:
            return self.data[child]
        #else:
            #print("No Child")
            
    def MinChild(self, index):
        Children = self.FindChild(index)
        if type(Children) == tuple:
            return min(Children)
        else:
            return Children
        
    def ExtractMin(self):
        self.data[0], self.data[-1] = self.data[-1], self.data[0] #Swap positions of first and last
        Min = self.data.pop() #Returns and removes last element i.e. minimum
        num = self.data[0]
        index = 0 #Set current index of num to bubble down
        target = self.MinChild(index) #Minimum of children
        while self.FindChild(index) != None and num > target: #Bubbling down
            child = self.data.index(target, index * 2 + 1)  #Find index of minimum of children
            self.data[index], self.data[child] = self.data[child], self.data[index] #Swapping
            index = child       
            target = self.MinChild(index)            
        return Min
        
    def Insert(self, num):
        self.data.append(num)
        index = len(self.data) - 1
        while index > 0 and num < self.FindParent(index):
            parent = (index + 1)//2 - 1
            self.data[parent], self.data[index] = self.data[index], self.data[parent]
            index = parent
        
        
    def Remove(self, index):
        self.data[index], self.data[-1] = self.data[-1], self.data[index]
        self.data.pop()
        num = self.data[index]
        if self.MinChild(index) != None:
            target = self.MinChild(index)
        while self.FindChild(index) != None and num > target:
            target = self.MinChild(index)
            child = self.data.index(target, index * 2 + 1)  #Find index of minimum of children
            self.data[index], self.data[child] = self.data[child], self.data[index] #Swapping
            index = child       
            
        
    #def __repr__(self):
    #    layers = math.floor(math.log2(len(self.data)))
    #    for layer in range(layers):
    #        start = 2 ** layer - 1
    #        print(start)
        
        
#%%
class MaxHeap:
    
    def __init__(self, data = []):
        self.data = data.copy()
    
    @classmethod
    def Heapify(cls, data = []):
        for root in range(len(data)//2-1, -1, -1):
            rootVal = data[root]
            child = root * 2 + 1
            while child < len(data):
                if child + 1 > len(data) and data[child] > data[child + 1]:
                    child +=1 #Finding minimum of 2 children
                if rootVal >= data[child]:
                    break
                data[child], data[(child-1)//2] = data[(child-1)//2], data[child]
                child = child * 2 + 1
        obj = cls(data)
        return obj
    
    def FindParent(self, index):
        assert index <= len(self.data) - 1, "Index out of range"
        parent = (index -1)//2
        return self.data[parent]
        
    def FindChild(self, index):
        child = index * 2 + 1
        if child + 1 <= len(self.data) - 1:
            return (self.data[child], self.data[child + 1])
        elif child == len(self.data) - 1:
            return self.data[child]
        #else:
            #print("No Child")
            
    def MaxChild(self, index):
        Children = self.FindChild(index)
        if type(Children) == tuple:
            return max(Children)
        else:
            return Children
        
    def ExtractMax(self):
        self.data[0], self.data[-1] = self.data[-1], self.data[0] #Swap positions of first and last
        Max = self.data.pop() #Returns and removes last element i.e. minimum
        num = self.data[0]
        index = 0 #Set current index of num to bubble down
        target = self.MaxChild(index) #Minimum of children
        while self.FindChild(index) != None and num < target: #Bubbling down
            child = self.data.index(target, index * 2 + 1)  #Find index of minimum of children
            self.data[index], self.data[child] = self.data[child], self.data[index] #Swapping
            index = child       
            target = self.MaxChild(index)            
        return Max
        
    def Insert(self, num):
        self.data.append(num)
        index = len(self.data) - 1
        while index > 0 and num > self.FindParent(index):
            parent = (index + 1)//2 - 1
            self.data[parent], self.data[index] = self.data[index], self.data[parent]
            index = parent
        
        
    def Remove(self, index):
        self.data[index], self.data[-1] = self.data[-1], self.data[index]
        self.data.pop()
        num = self.data[index]
        if self.MinChild(index) != None:
            target = self.MaxChild(index)
        while self.FindChild(index) != None and num < target:
            target = self.MaxChild(index)
            child = self.data.index(target, index * 2 + 1)  #Find index of minimum of children
            self.data[index], self.data[child] = self.data[child], self.data[index] #Swapping
            index = child     
        
#%% Or fuck this
import heapq