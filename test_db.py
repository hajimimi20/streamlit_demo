import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="acc_passwd",
    charset="utf8mb4"
)

print("MariaDB 連線成功！")

connection.close()