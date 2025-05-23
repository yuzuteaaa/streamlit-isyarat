from pymongo import MongoClient

def get_db():
    client = MongoClient("mongodb+srv://abdulmuhith:RSOhuo1jLS5l0aei@cluster0.5ha8rrf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client["sign_language_db"]
    return db
