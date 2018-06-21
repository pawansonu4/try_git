from itertools import combinations
x1=input().rstrip().split(' ')
y=[]
for i in range(int(x1[1])):
    y[i]=list(combinations(x1[0],i+1))
print(y)