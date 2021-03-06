import os
from flask import Flask
from flask_restful import Api
from resources.item import Item, ItemList
from resources.frienditem import FriendItem, FriendItemList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'veer'
api = Api(app)

api.add_resource(Item, '/fire/<string:phonenumber>')
api.add_resource(ItemList, '/fires')
api.add_resource(FriendItem, '/friend/<string:phonedigits>')
api.add_resource(FriendItemList, '/friends')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
