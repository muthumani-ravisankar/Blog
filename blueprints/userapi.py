from flask import Blueprint , request, session
from src.auth.Users import Users, customError
bp= Blueprint("userapi",__name__)
@bp.route('/signup',methods=['POST','GET'])
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


@bp.route('/login',methods=['POST','GET'])
def login():
    if(request.method == 'GET'):
        return {
            'message':'Method not found , use POST method'
        },405
    
    if session.get('islogged'):
        return{
            'message':'Already authenticated'
        },202

    if('username' in request.form and 'password' in request.form):
        username = request.form['username']
        password = request.form['password']
        try:
            result = Users.authenticate(username,password)
            return {
                'message':'login success',
                'user id': result
            },200
        except customError as e:
            return{
                'Exception':str(e)
            },400
    else:
        return {
            'message':'Not enough parameters'
        },400

@bp.route('/logout',methods=['GET'])
def logout():
    if session.get('islogged'):
        session['islogged']=False
        return {
            'message':'logged out Successfully'
        },200
    else:
        return {
            'message':'You are not authenticated'
        },401
    
@bp.route('/getusers')
def getusers():
    if session.get('islogged'):
        result =Users.getUsers()
        return result,200
    else:
        return {
            "message":"You are not authenticated"
        },401