from flask import json,Response,jsonify,Blueprint,request
from flask_jwt_extended import create_access_token,jwt_required,get_jwt_identity
from util.util_encoder import UtilEncoder
from service.user_service import UserService

app_user = Blueprint("app_user",__name__)

user_service = UserService()


@jwt_required()
@app_user.route('/user/login', methods=['POST'])
def login():
    try:
        data = request.json
        user = user_service.login(data)
        acces_token = create_access_token(identity={'user':user})
        return jsonify({'token':acces_token})
    except Exception as e:
        return jsonify({'message':str(e)})

@app_user.route("/user")
def get_users():
    return Response(status=200,mimetype="application/json",
                    response=json.dumps(user_service.get_users(), cls=UtilEncoder))

@app_user.route("/game")
def game():
    return Response(status=200, mimetype="application/json",
                    response=json.dumps(user_service.game(), cls=UtilEncoder))