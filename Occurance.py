arr = [-4, 3, -9, 0, 4, 1]

pos = []
neg = []
z = []

for i in arr:
    if i>0:
        pos.append(i)
    elif i<0:
        neg.append(i)
    elif i==0:
        z.append(i)



print(round(len(pos)/len(arr),6))
print(round(len(neg)/len(arr),6))
print(round(len(z)/len(arr),6))
