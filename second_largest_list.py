x=input("Enter list values separated by space:")
l=x.split(" ")
for _ in range(len(l)):
    try:
        for i in range(len(l)):
            if int(l[i]) > int(l[i+1]):
                c=l[i+1]
                l[i + 1]=l[i]
                l[i]=c
    except IndexError:
        pass
print(l)

