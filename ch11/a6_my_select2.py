import pymysql, sys
try:
    con = pymysql.connect(host="127.0.0.1", port=3306, user="root", password='mysql', db='test', charset='utf8')
    cursor = con.cursor()  # 자바의 Statement, PreparedStatement / sql을 위한 객체
    cursor.execute("select * from dept order by deptno")
    data = cursor.fetchall()
    print(data)
    for i in data:
        print(i)
except:
    print("예외 : ", sys.exc_info())
finally:
    cursor.close()
    con.close()