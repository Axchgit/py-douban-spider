'''
@Description: 
@Author: Dragon
@Email: 123@123.com
@Date: 2020-05-27 15:53:42
@LastEditTime: 2020-05-27 17:57:30
@LastEditors: Dragon
'''

import pymysql
# 连接数据库

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='pytest',
    charset='utf8'
)

# 创建游标对象
cur = conn.cursor()

try:
    create_sqli =  create_sqli = "CREATE TABLE `test3` ( `id` INT NOT NULL AUTO_INCREMENT , `name` VARCHAR(20) NOT NULL , bd text NOT NULL , PRIMARY KEY (`id`));"
    cur.execute(create_sqli)
except Exception as e:
    print("创建数据表失败:", e)
else:
    print("创建数据表成功;")

# try:
#     insert_sqli = "insert into hello values(2, 'fensi');"
#     cur.execute(insert_sqli)
# except Exception as e:
#     print("插入数据失败:", e)
# else:
#     # 如果是插入数据， 一定要提交数据， 不然数据库中找不到要插入的数据;
#     conn.commit()
#     print("插入数据成功;")
