lst=[5,6,7,8]
strfile=r'C:\Users\Pawan\Downloads\untitled\temp_bin.txt'
buffer=bytes(lst)
print(buffer)

with open(strfile,'wb') as f:
    f.write(buffer)

print("written file, reading it again")
with open(strfile,'rb') as f:
    buffer=f.read()
    for i in buffer:
        print(i)
