from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from resources.fooditems import FoodItems

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'abcd@1234'
api = Api(app)


api.add_resource(FoodItems, '/items')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
