file = r"C:\Users\foobe\Documents\Algorithms\Part 1\Section 6\integers.txt"

HT = {}

with open(file, 'r') as f:
    for line in f.readlines():
        num = int(line)
        HT[num] = True
        
#%%
target = range(-10000, 10000 + 1)

count = 0

#%%
for t in target:
    for x in HT:
        y = t - x
        if y == x:
            print("Dupe")
            continue
        if HT.get(y):
            count += 1
            break

print(count)

#%%
for x in HT:
    print(x)
    