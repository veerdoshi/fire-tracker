from flask_restful import Resource, reqparse
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('magnitude',
        type=float,
        required=True,
        help='This field cannot be left blank!'
    )


    def get(self, name):
        item = ItemModel.find_by_measure(name)
        if item:
            return quakeitem.json()

    def post(self, name):
        data = Item.parser.parse_args()
        item = ItemModel(name, data['magnitude'])
        item.save_to_db()
        return item.json(), 201

class ItemList(Resource):
    def get(self):
         return {'items': [quakeitem.json() for quakeitem in ItemModel.query.all()]}
