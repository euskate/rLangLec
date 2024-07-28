from pymongo import MongoClient

# 데이터베이스 연결
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# 데이터 삽입
collection.insert_one({'name': 'John Doe', 'position': 'Engineer'})

# 데이터 조회
for doc in collection.find():
    print(doc)