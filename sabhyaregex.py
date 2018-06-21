import re


x="helen"
y="beaver"

# Delete Python-style comments

x1=re.sub(r'e(.)e', 'a\g<1>a', x)
print(x1)

