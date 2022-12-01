import pymysql
sql_conn=pymysql.connect(user='root',password='sushmit@saatvik2204',host='localhost',database='emp_info')
sql_cu=sql_conn.cursor()

a=[['1','2','3'],['4','5','6']]
print(a[0][1])


sql_conn.commit()
sql_conn.close()

