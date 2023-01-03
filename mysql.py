import pymysql
sql_conn=pymysql.connect(user='root', password='sushmit@saatvik2204',host='localhost',database='emp_info')
sql_cu=sql_conn.cursor()
#print(sql_cu.execute('show databases'))
#print(sql_cu.fetchall())
#print(sql_cu.execute("insert into emp_personal values('bala','bala@gmail.com','chennai','98765409')"))
#print(sql_cu.fetchall())
#print(sql_cu.execute("select * from emp_personal where emp_name='sushmita'"))
#print(sql_cu.fetchall())
print(sql_cu.execute("update emp_personal set emp_mobile='6976976' where emp_name='chand'"))

sql_conn.commit()
sql_conn.close()


