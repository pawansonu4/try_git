#!/Python36/python
import cgi, cgitb

form=cgi.FieldStorage()
#Fetch form data
first_name=form.getvalue('first_name')
last_name=form.getvalue('last_name')

print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<title>Hello - Second CGI</title>")
print("</head")
print("<body>")
print("<h2>Hello %s %s</h2>" % (first_name,last_name))
print("</body>")
print("</html>")