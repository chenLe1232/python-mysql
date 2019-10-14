import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="lechen9527",
        database="demo"
    )
    con.start_transaction()
    cursor = con.cursor()
    sql = "INSERT INTO t_emp(empno,ename,job,mgr,hiredate,sal,comm,deptno) VALUES(%s,%s,%s, %s,%s,%s,%s,%s)"
    cursor.execute(sql, (9600,"赵楠","SALESMAN", None,"1985-12-1",2500,None,10))
    con.commit()
except Exception as e:
    # 如果在try语句中出现问题，事务进行回滚一下
    if "con" in dir():
        con.rollback()
    print(e)

finally:
    if "con" in dir():
        con.close