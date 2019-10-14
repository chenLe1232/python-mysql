import mysql.connector.pooling

config = {
    "host": "localhost",
    "port": "3306",
    "user": "root",
    "password": "lechen9527",
    "database": "demo"
}
try:
    # 进行连接池连接
    pool = mysql.connector.pooling.MySQLConnectionPool(**config, pool_size=10)
    # pool.get_connection该语句为从连接池中获取连接，根据该连接创建游标后执行sql语句等等操作。
    con = pool.get_connection()
    con.start_transaction()
    # 创建游标
    cursor = con.cursor()
    sql = "UPDATE t_emp SET sal=sal+%s WHERE deptno=%s"
    cursor.execute(sql, (1000, 50))
    # 事务提交
    con.commit()
# 错误信息
except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)
