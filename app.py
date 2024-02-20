import pymongo
from flask import Flask, request, Response , session
# from gridfs import GridFS, GridFSBucket
import mimetypes
import uuid
import os
from src import getConfig
from src.auth.Users import Users ,customError
from blueprints import userapi , blogapi
app = Flask(__name__)
app.secret_key=getConfig('secret_Key')
app.register_blueprint(userapi.bp)
app.register_blueprint(blogapi.bp)

@app.route('/hello')
def hello_world():
   return 'Hello World'

if __name__ == '__main__':
   app.run(debug=True)