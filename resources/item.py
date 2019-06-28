from flask_restful import Resource, reqparse
from models.item import ItemModel
import simplejson as json

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
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

        friendsinformationstring = '{"friends":[]}'
        friendsObj = json.loads(friendsinformationstring)

        if '+' not in phonenumber:
            item = ItemModel.find_by_measure(phonenumber)
            if item:
                friendsObj['friends'].append(item)
        else:
            x = phonenumber.split("+")
            for y in range(0,len(x)):
                friendsObj['friends'].append([item.json() for item in ItemModel.query.filter_by(phonenumber=x[y]).all()])
        return friendsObj

        #item = ItemModel.find_by_measure(phonenumber)
        #if item:
        #    return item.json()

    #def post(self, name):
    def post(self, phonenumber):
        data = Item.parser.parse_args()
        item = ItemModel(phonenumber, data['name'], data['latitude'], data['longitude'])
        item.save_to_db()
        return item.json(), 201

    #def delete(self, name):
    def delete(self, phonenumber):
        item = ItemModel.find_by_measure(phonenumber)
        if item:
            item.delete_from_db()
        return {'message': 'Deleted'}

    def put(self, phonenumber):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_measure(phonenumber)

        if item is None:
            item = ItemModel(phonenumber, data['name'], data['latitude'], data['longitude'])
        else:
            item.name = data['name']
            item.latitude = data['latitude']
            item.longitude = data['longitude']


        item.save_to_db()

        return item.json()



class ItemList(Resource):
    def get(self):
         return {'fires': [item.json() for item in ItemModel.query.all()]}
