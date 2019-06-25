from flask_restful import Resource, reqparse
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('phonenumber',
        type=str,
        required=True,
        help='This field cannot be left blank!'
    )
    parser.add_argument('latitude',
        type=float,
        required=True,
        help='This field cannot be left blank!'
    )
    parser.add_argument('longitude',
        type=float,
        required=True,
        help='This field cannot be left blank!'
    )

    #def get(self, name):
    def get(self, phonenumber):
        item = ItemModel.find_by_measure(phonenumber)
        if item:
            return item.json()

    def post(self, name):
        data = Item.parser.parse_args()
        item = ItemModel(name, data['phonenumber'], data['latitude'], data['longitude'])
        item.save_to_db()
        return item.json(), 201

    #def delete(self, name):
    def delete(self, phonenumber):
        item = ItemModel.find_by_measure(phonenumber)
        if item:
            item.delete_from_db()
        return {'message': 'Deleted'}

    def put(self, name, phonenumber):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_measure(phonenumber)

        if item is None:
            item = ItemModel(name, data['phonenumber'], data['latitude'], data['longitude'])
        else:
            item.phonenumber = data['phonenumber']
            item.latitude = data['latitude']
            item.longitude = data['longitude']


        item.save_to_db()

        return item.json()



class ItemList(Resource):
    def get(self):
         return {'fires': [item.json() for item in ItemModel.query.all()]}
