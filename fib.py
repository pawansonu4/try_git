x=input("Enter count")
def fib(x):
    a,b=0,1
    result_list=[]
    result_list.append(a)
    result_list.append(b)
    for i in range(int(x)-2):
        result_list.append(result_list[i]+result_list[i+1])

    return  result_list

y=fib(x)
print(y)