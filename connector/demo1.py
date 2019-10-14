import mysql.connector
con = mysql.connector.connect(
    host="localhost", port="3306",
    user="root", password="lechen9527",
    database="demo"
)

cursor = con.cursor()
sql = "SELECT empno,ename, hiredate FROM t_emp"
cursor.execute(sql)
print(cursor)
for one in cursor:
    print(one[0], one[1], one[2])
# 数据用完之后 如果不使用的话，要进行关闭 即con.close()
con.close()
