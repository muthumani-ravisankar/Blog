from flask import Flask, request, Response , session,jsonify
from src.database import database
import uuid
from time import time
from random import randint
db = database.getConnection()
users = db.users

class customError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Blog:

    @staticmethod
    def createBlog(user_id, blog_tittle, blog_content):
        user=users.find_one({"_id":user_id})
        if(user ):
                blog_id = str(uuid.uuid4())
                new_blog={
                     "blog_id":blog_id,
                     "blog_tittle":blog_tittle,
                     "blog_content":blog_content,
                     "created_at":time()
                }
                user['blogs'].append(new_blog)
                users.update_one({'_id': user_id}, {'$set': {'blogs': user['blogs']}})
                return {"bid":str(blog_id),
                        "tittle":str(blog_tittle)}
                

        else:
             raise customError("userid: {} does not exist".format(user_id)) 

    @staticmethod
    def deleteBlog(user_id,blog_id):
        user=users.find_one({"_id":user_id})
        if(user ):
                users.update_one({'_id': user_id}, {'$set': {'blogs': user['blogs']}})
                result = users.update_one(
                                {'_id': user_id},
                                {'$pull': {'blogs': {'blog_id': blog_id}}}
                        )
                if result.modified_count > 0:
                             return {"bid":str(blog_id)}
                else:
                      raise customError("Blog not found ")
        else:
             raise customError("userid: {} does not exist".format(user_id)) 
        
    @staticmethod
    def readBlog(user_id):
        user=users.find_one({"_id":user_id})
        if(user):
            blogs = user.get('blogs', [])
            return jsonify(blogs)
        else:
            raise customError("userid: {} does not exist".format(user_id)) 

    @staticmethod
    def getBlog(user_id, blog_id):
        user = users.find_one({'_id': user_id})
        if user:
            # Find the blog by blog_id in the user's blogs array
            blog = next((blog for blog in user.get('blogs', []) if str(blog.get('blog_id')) == blog_id), None)
            if blog:
                return jsonify(blog)
            else:
               raise customError("Blog not found ")
        else:
            raise customError("userid: {} does not exist".format(user_id))
      
    @staticmethod
    def editBlog(u_id,b_id,b_tittle,b_content):
        user=users.find_one({"_id":u_id})
        if user:
            blog = next((blog for blog in user.get('blogs', []) if str(blog.get('blog_id')) == b_id), None)
            result=users.update_one(
            {
                "_id": u_id,
                "blogs.blog_id": b_id
            },
            {
                "$set": {
                "blogs.$.blog_tittle": b_tittle,
                "blogs.$.blog_content": b_content,
                "blogs.$.updated_at": time()
                }
            }
            )
            return result
            

        else:
            raise customError("userid: {} does not exist".format(u_id))
              
  