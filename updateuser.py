# import pymongo
from pymongo import MongoClient

class Update():
    #connect to my mongoDB collections
    client = MongoClient('mongodb+srv://shayshmaiser:PmRtpwEnX6CldTMb@players.tplziu7.mongodb.net/')
    db = client["bikorotDB"]
    collection = db["Users"]

    #replace with real input !!!!!
    input_username = input("enter username: ")
    input_password = input("enter password: ")


    #updateuser
    input_password2 = input("unter new password: ")
    post_updateuser1 = {"username": input_username, "password": input_password}
    verify_input_forupdate = collection.find_one(post_updateuser1)
    if verify_input_forupdate:
        print("User updated successfully")
        input_updateuser = collection.update_one(post_updateuser1, {"$set": {"password": input_password2}})
    else: 
        print("User not found")




