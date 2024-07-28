import mysql.connector

# 데이터베이스 연결
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="company",
    port=3306
)

cursor = db_connection.cursor()

# 테이블 생성 (이미 생성된 경우 생략 가능)
cursor.execute("""
CREATE TABLE IF NOT EXISTS naver (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255)
)
""")

# 데이터 삽입
insert_query = "INSERT INTO naver (title) VALUES (%s)"
cursor.execute(insert_query, (title,))
db_connection.commit()

# 연결 종료
cursor.close()
db_connection.close()
