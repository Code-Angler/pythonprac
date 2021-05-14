from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# [insert / find / update / delete]

# [insert]

doc = {'name':'jane','age':21}
db.users.insert_one(doc)

# [find several factor]

same_ages = list(db.users.find({'age':21},{'_id':False}))
same_ages = list(db.users.find({},{'_id':False})) # all dict, use empty {} instead of {'age':21}

# [call individual factor]

for person in same_ages:
print(person)

# [find one factor]

user = db.users.find_one({'name':'bobby'})
print(user['age'])

# [update]

db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
db.users.update_many({'name':'bobby'},{'$set':{'age':19}}) # update all factor which fit condition


# [delete]

db.users.delete_one({'name':'john'})
db.users.delete_many({'name':'john'}) # delete all factor which fit condition



