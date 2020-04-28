import pymysql
import pandas as pd

# MySQL Connection
# Google Cloud Platform - Database Instance External IP Addr. : 34.82.158.37
# default port number : 3306
try:
    db_connection = pymysql.connect(host='34.82.158.37', user='dev1', password='dev2020', db='myasset', charset='utf8')
except Exception as e:
    print(e)

# Cursor object
# cursor = db_connection.cursor()
# DictCursor object
cursor = db_connection.cursor(pymysql.cursors.DictCursor)

# SQL문 실행
sql = "select * from common_code_hdr"
cursor.execute(sql)

# 데이타 Fetch
result = cursor.fetchall()
print(result)  # 전체 rows
# print(rows[0])  # 첫번째 row: (1, '김정수', 1, '서울')
# print(rows[1])  # 두번째 row: (2, '강수정', 2, '서울')
frame_result = pd.DataFrame(result)
frame_result
# Connection 닫기
db_connection.close()