from flask_restful import Resource, reqparse
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('magnitude',
        type=integer,
        required=True,
        help='This field cannot be left blank!'
    )

    def get(self, name):
        item = ItemModel.find_by_measure(name)
        if item:
            return item.json()

    def post(self, name):
        data = Item.parser.parse_args()
        item = ItemModel(name, data['magnitude'])
        item.save_to_db()
        return item.json(), 201
    
    def delete(self, name):
        item = ItemModel.find_by_measure(name)
        if item:
            item.delete_from_db()
        return {'message': 'Quake deleted'}

class ItemList(Resource):
    def get(self):
         return {'quakes': [item.json() for item in ItemModel.query.all()]}
