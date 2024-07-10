from pymongo import MongoClient

class Createuser:
    # Connect to my MongoDB collections
    client = MongoClient('mongodb+srv://shayshmaiser:PmRtpwEnX6CldTMb@players.tplziu7.mongodb.net/')  # Highlighted
    db = client["bikorotDB"]  
    collection = db["Users"]  

    def __init__(self, input_username, input_password):
        self.input_username = input_username
        self.input_password = input_password

    def create(self, input_username, input_password):
        # Create user
        post_createuser = {"username": input_username, "password": input_password}
        self.collection.insert_one(post_createuser)  
        print("User created")