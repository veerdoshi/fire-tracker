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
        #frienditem = FriendItemModel.find_by_measure(phonedigits)
        return {'friends': [frienditem.json() for frienditem in FriendItemModel.query.filter_by(phonedigits=phonedigits).all()]}

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
        frienditem = FriendItemModel.find_by_measure(phonedigits)
        if frienditem:
            frienditem.delete_from_db()
        return {'message': 'Deleted'}

    def put(self, phonedigits):
        frienddata = FriendItem.parser.parse_args()

        frienditem = FriendItemModel.find_by_measure(phonedigits)

        if frienditem is None:
            frienditem = FriendItemModel(phonedigits, frienddata['friendname'], frienddata['friendphone'])
        else:
            frienditem.friendname = frienddata['friendname']
            frienditem.friendphone = frienddata['friendphone']


        frienditem.save_to_db()

        return frienditem.json()



class FriendItemList(Resource):
    def get(self):
         return {'friends': [frienditem.json() for frienditem in FriendItemModel.query.all()]}
