# import pymongo
from pymongo import MongoClient

class Login():
    #connect to my mongoDB collections
    client = MongoClient('mongodb+srv://shayshmaiser:PmRtpwEnX6CldTMb@players.tplziu7.mongodb.net/')
    db = client["bikorotDB"]
    collection = db["Users"]

    #replace with real input !!!!!
    input_username = input("enter username: ")
    input_password = input("enter password: ")


    #login
    post_login = {"username": input_username, "password": input_password}
    input_login = collection.find_one(post_login)
    if input_login:
        print("Login successful:")
        for x in input_login:
            print(x)
    else: 
        print("Login failed")
    #mongoDB example: 
    # filter={}
    # result = client['bikorotDB']['Users'].find(
    #   filter=filter
    # )








