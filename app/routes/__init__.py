from flask_restful import Api
from app.controllers import (
    IndexView, UserView, UserDetailView, UserLoginView)


api = Api()

# Index route
api.add_resource(IndexView, '/')

# User routes
api.add_resource(UserView, '/users', endpoint='users')
api.add_resource(UserDetailView, '/users/<string:user_id>',
                 endpoint='user')
api.add_resource(UserLoginView, '/users/login', endpoint='user_login')
