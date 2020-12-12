import os

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.fooditems import FoodItems
from resources.messmenu import MessMenu
from resources.user import UserRegister, UserLogin, Users

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'abcd@1234'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWTManager(app)


api.add_resource(FoodItems, '/items')
api.add_resource(MessMenu, '/menu/<string:user_id>')
api.add_resource(UserRegister, '/signup')
api.add_resource(UserLogin, '/login')
api.add_resource(Users, '/users')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)