t = 0
t1 = 0
for i in range(len(apples)):
    temp = a + apples[i]
    if (temp in range(s, t + 1)):
        t += 1
for i in range(len(oranges)):
    temp = b + oranges[i]
    if (temp in range(s, t + 1)):
        t1 += 1
print(t)
print(t1)
