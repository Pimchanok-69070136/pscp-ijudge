a = [1,2,3]
b = [10,25,3]

print(sum(i*j for i,j in zip(a,b)))

totalsum = 0

for i,j in zip(a,b):
    totalsum += i*j

print(totalsum)