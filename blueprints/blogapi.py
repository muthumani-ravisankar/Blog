from flask import Blueprint , request, session, jsonify
from src.blog.Blog import Blog,customError
bp= Blueprint("blogapi",__name__,url_prefix="/blogs")
@bp.route('/create',methods=['POST'])
def create():
    if(request.method =='GET'):
        return{
            'message':'Method not found  use POST method'
        },405
    if session.get("islogged") and request.method=='POST':
        if('blog_tittle' in request.form and 'blog_content' in request.form ):
                blog_tittle = request.form['blog_tittle']
                blog_content = request.form['blog_content']
                try:
                    result= Blog.createBlog(session["uid"],blog_tittle,blog_content)
                    return {'message':'blog created successfully',
                            'blog_id':result['bid'],
                            'blog_tittle':result['tittle'],
                            },200
                except customError as e:
                    return {'exception':str(e)}
        else:
            return{
                'message':'Not enough parameterst'
            },400
    else:
        return{
            'message':'You are not authenticated'
        },401



@bp.route('/delete',methods=['POST','GET'])
def delete():    
    if session.get('islogged'):
        if 'blog_id' in request.args:
            blog_id = request.args.get('blog_id')
            try:
                result = Blog.deleteBlog(session['uid'],blog_id)
                return {
                    'message':'blog deleted successfully.',
                    'blog id': blog_id
                },200
            except customError as e:
                return{
                    'Exception':str(e)
                },400
        else:
            return {
                'message':'Not enough parameters'
            },400
    else:
        return {
            'message':'You are not authenticated'
        },401


@bp.route('/read',methods=['GET'])
def read():
    if session.get('islogged'):
        try:
            result= Blog.readBlog(session['uid'])    
            return result,200
        except customError as e:
            return {
                'Exception':str(e)
            },401
    else:
        return {
            'message':'You are not authenticaated'
        }
@bp.route('/getblog',methods=['GET'])
def getblog():
    if session.get('islogged'):
        if request.args.get('blog_id'):
            blog_id=request.args.get('blog_id')
            try:
                result=Blog.getBlog(session['uid'],blog_id)
                return result,200
            except customError as e:
                return {
                    'Exception': str(e)
                },400
        else:
            return {
                "message":"require <blog_id> in GET params"
            }

    else:
        return {
            'message':'You are not authenticated'
        }
    
@bp.route('/editblog',methods=['POST'])
def editblog():
    if session.get('islogged'):
        if('blog_tittle' in request.form and 'blog_content' in request.form and 'blog_id' in request.form ):
            blog_tittle = request.form['blog_tittle']
            blog_content = request.form['blog_content']
            blog_id = request.form['blog_id']
            try:
                result=Blog.editBlog(session['uid'],blog_id,blog_tittle,blog_content)
                if result:
                    return {
                        "message":"Blog updated successfully.",
                        "blog_id":blog_id
                    }
            except customError as e:
                return {
                    'Exception': str(e)
                },400
        else:
            return {
                'message':'Not enough parameters'
            }

    else:
        return {
            'message':'You are not authenticated'
        }