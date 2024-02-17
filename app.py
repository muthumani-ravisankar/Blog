import pymongo
from flask import Flask, request, Response , session
# from gridfs import GridFS, GridFSBucket
import mimetypes
import uuid
import os
from src.auth.Users import Users ,customError
app = Flask(__name__)

@app.route('/hello')
def hello_world():
   return 'Hello World'

@app.route('/signup',methods=['POST','GET'])
def signup():
    if(request.method =='GET'):
        return{
            'message':'Method not found , use POST method'
        },405
    if('username' in request.form and 'email' in request.form and 'confirm_password' in request.form and'password' in request.form):
            username = request.form['username']
            password = request.form['password']
            confirm_password= request.form['confirm_password']
            email = request.form['email']
            try:
                #TODO: get the confirm password from the user
                result= Users.register(username,password,confirm_password,email)
                return {'message':'signup success'},200
            except customError as e:
                return {'exception':str(e)}
    else:
        return{
            'message':'Not enough parameterst'
        },400


@app.route('/login',methods=['POST','GET'])
def login():
    if(request.method == 'GET'):
        return {
            'message':'Method not found , use POST method'
        },405
    

    if('username' in request.form and 'password' in request.form):
        username = request.form['username']
        password = request.form['password']
        try:
            result = Users.athunticate(username,password)
            return {
                'message':'login success',
                'session id': result
            },200
        except customError as e:
            return{
                'Exception':str(e)
            },400
    else:
        return {
            'message':'Not enough parameters'
        },400


if __name__ == '__main__':
   app.run()