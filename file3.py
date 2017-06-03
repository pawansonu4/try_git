fo = open("foo.txt", "wb")
y=bytes("Python is a great language.\nYeah its great!!\n","utf-8")
fo.write(y)
# Close opend file
fo.close()