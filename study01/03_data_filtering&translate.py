import pandas as pd

# MySQL에서 데이터 읽어오기
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="company",
    port=3306
)

query = "SELECT * FROM naver"
data = pd.read_sql(query, db_connection)

# 데이터 정제 및 변환 (예: 문자열로 변환)
data['title'] = data['title'].str.strip()

# 데이터 확인
print(data.head())

# 연결 종료
db_connection.close()
