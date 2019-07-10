from flask_restful import Resource, reqparse
from models.frienditem import FriendItemModel

class FriendItem(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('friendname',
        type=str,
        required=True,
        help='This field cannot be left blank!'
    )
    parser.add_argument('friendphone',
        type=str,
        required=True,
        help='This field cannot be left blank!'
    )

    def get(self, phonedigits):

        if '-' not in phonedigits:
            return {'friends': [frienditem.json() for frienditem in FriendItemModel.query.filter_by(phonedigits=phonedigits).all()]}
        else:
            x = phonedigits.split("-")
            friendJSON = [frienditem.json() for frienditem in FriendItemModel.query.filter_by(phonedigits=x[0],friendphone=x[1]).all()]
            return {'friends': friendJSON}
            #return {'friends': [friendJSON for friendJSON in FriendItemModel.query.filter_by(friendphone=x[1]).all()]}

        #frienditem = FriendItemModel.find_by_measure(phonedigits)

        #return {'friends': [frienditem.json() for frienditem in FriendItemModel.query.filter_by(phonedigits=phonedigits).all()]}

#        frienditem = FriendItemModel.find_by_measure(phonedigits)
#        if frienditem:
#            return frienditem.json()

    #def post(self, name):
    def post(self, phonedigits):
        frienddata = FriendItem.parser.parse_args()
        frienditem = FriendItemModel(phonedigits, frienddata['friendname'], frienddata['friendphone'])
        frienditem.save_to_db()
        return frienditem.json(), 201

    #def delete(self, name):
    def delete(self, phonedigits):
        frienddata = FriendItem.parser.parse_args()
        frienditem = FriendItemModel.find_by_measure(phonedigits)
        if frienditem:
            frienditem.delete_from_db()
            return {'message': 'Deleted'}
        else:
            return {'message': 'Item not found'}
    def put(self, phonedigits):
        frienddata = FriendItem.parser.parse_args()

        y = phonedigits.split("-")
        #frienditem = FriendItemModel.query.filter_by(phonedigits=y[0],friendphone=y[1]).all()

        frienditem = FriendItemModel.query.filter_by(phonedigits=y[0], friendphone=y[1]).all()
        #frienditem = FriendItemModel.find_by_measure(phonedigits)

        if frienditem is None:
            #y = phonedigits.split("-")
            frienditem = FriendItemModel(y[0], frienddata['friendname'], frienddata['friendphone'])
        else:
            #frienditem.friendname = frienddata['friendname']
            #frienditem.friendphone = frienddata['friendphone']
            print("HI")

        frienditem.save_to_db()

        return frienditem.json()



class FriendItemList(Resource):
    def get(self):
         return {'friends': [frienditem.json() for frienditem in FriendItemModel.query.all()]}
