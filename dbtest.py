import pymysql
db=pymysql.connect("localhost","root","admin","testdb")
cursor=db.cursor()
cursor.execute("select version()")
data=cursor.fetchone()
print("Database Version: %s" % data)
db.close()