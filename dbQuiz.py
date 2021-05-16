from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

matrix_score = (db.movies.find_one({'title':'매트릭스'}))['point']
print(matrix_score)

same_point = list(db.movies.find({'point':matrix_score}))

for s_m in same_point:
    s_point_m = s_m['title']
    print(s_point_m)

# db.movies.update_one({'title':'매트릭스'},{'$set':{'point':'0'}})
