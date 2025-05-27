from pymongo import MongoClient

def get_db():
    client = MongoClient("mongodb+srv://baisyufan:nzPoNISBiZxLIKbn@bais.5y9mhli.mongodb.net/")
    db = client["backend-capstone"]
    return db