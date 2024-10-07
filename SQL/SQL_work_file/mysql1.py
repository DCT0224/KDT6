import pymysql
import pandas as pd

conn = pymysql.connect(host='localhost',user='root',password='1234',db='sakila',charset='utf8')

cur = conn.cursor(pymysql.cursors.DictCursor) # ()안에 pymysql.cursors.DictCursor 넣으면 column 정보도 같이 출력됨. 
cur.execute('select * from language')
rows = cur.fetchall()
print(rows)

language_df = pd.DataFrame(rows)
print(language_df)

cur.close()
conn.close()