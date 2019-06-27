from db import db

class FriendItemModel(db.Model):
    __tablename__ = 'friendItems'

    num = db.Column(db.Integer, primary_key=True)
    phonedigits = db.Column(db.String(80))
    friendname = db.Column(db.String(80))

    def __init__(self, phonenumber):
        self.phonedigits = phonedigits
        self.friendname = friendname
#        self.num = num
    def json(self):
        return {'phonedigits': self.phonedigits, 'friendname': self.friendname}

    @classmethod
    #def find_by_measure(cls, name):
    def find_by_measure(cls, phonedigits):
       #return cls.query.filter_by(name=name).first()
       return cls.query.filter_by(phonedigits=phonedigits).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
