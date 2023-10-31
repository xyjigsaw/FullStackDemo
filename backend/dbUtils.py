# Name: dbUtils.py
# Author: Reacubeth
# Time: 2023/10/31 20:40
# Mail: noverfitting@gmail.com
# Site: www.omegaxyz.com
# -- coding: utf-8 --**

import pymysql

# 连接配置信息
config = {
    'host': 'localhost',
    'port': 3306,  # MySQL默认端口
    'user': 'root',  # mysql默认用户名
    'password': '12345678',
    'db': 'paper_db',  # 数据库
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}


def db_get_paper(num=10):
    try:
        con = pymysql.connect(**config)
        sql = "SELECT * FROM am_paper limit %d" % num
        with con.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            con.close()
        return result
    except Exception as e:
        print(e)
        return []


