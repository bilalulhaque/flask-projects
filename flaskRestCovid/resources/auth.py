from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
import os
import datetime


class SignInApi(Resource):
 def post(self):
   body = request.get_json()
   user = os.environ.get('user_email')
   authorized = os.environ.get('user_password')
   if body.get('password') != authorized or body.get('email') != user:
     return {'error': 'Email or password invalid'}, 401


   expires = datetime.timedelta(days=7)
   access_token = create_access_token(identity=str(1), expires_delta=expires)
   return {'token': access_token}, 200