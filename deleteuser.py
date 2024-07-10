# import pymongo
from pymongo import MongoClient

class Delete():
    #connect to my mongoDB collections
    client = MongoClient('mongodb+srv://shayshmaiser:PmRtpwEnX6CldTMb@players.tplziu7.mongodb.net/')
    db = client["bikorotDB"]
    collection = db["Users"]

    #replace with real input !!!!!
    input_username = input("enter username: ")
    input_password = input("enter password: ")


    #deleteuser
    post_deleteuser = {"username": input_username, "password": input_password}
    verify_input = collection.find_one(post_deleteuser)
    if verify_input:
        print("User deleted successfully")
        input_deleteuser = collection.delete_one(post_deleteuser)
    else: 
        print("User not found")






