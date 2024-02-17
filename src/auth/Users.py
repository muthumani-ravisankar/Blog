from flask import Flask, request, Response , session
from src.database import database
import bcrypt
from time import time
from random import randint
db = database.getConnection()
users = db.users

class customError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Users:
    def welcome(self,name):
        return ("Welcome {} !".format(name))
    
    @staticmethod
    def register(username, password, confirm_password,email):
        # TODO: Avoid duplicate signups
    

        user=users.find_one({"username":username})
        mail=users.find_one({"email":email})
        if(not user ):
            if(not mail):
                if password != confirm_password:
                    raise customError("Password and Confirm Password do not match")
                password = password.encode()
                salt = bcrypt.gensalt() # like a secret key that is embedded into the password for verification purposes while logging in
                password = bcrypt.hashpw(password, salt)    
                _id = users.insert_one({
                    "username": username, # TODO: Make as unique index to avoid duplicate entries
                    "password": password,
                    "email":email,
                    "register_time": time(),
                    "active": False,
                    "activate_token": randint(100000, 999999)           
                }) 
            else:
                raise customError("email {} already exist".format(email)) 

        else:
             raise customError("username {} already exist".format(username)) 
        
        # we should send this OTP (activate_token) via SMS or Email to the user
        # TODO: Use gmail to send emails with OTP
        
        return str(username)
    
    @staticmethod
    def athunticate(username,password):
        result = users.find_one({
            'username':username
        })

        if result:
            password_hash = result['password']
            if(bcrypt.checkpw(password.encode(),password_hash)):
                #TODO: Register a session and return a session id on successful login
               return str(username)
            else:
                raise customError('Incorrect password')
        else:
            raise customError("Invalid credential")

