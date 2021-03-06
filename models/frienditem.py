from db import db

class FriendItemModel(db.Model):
    __tablename__ = 'friendItems'

    num = db.Column(db.Integer, primary_key=True)
    phonedigits = db.Column(db.String(80))
    friendname = db.Column(db.String(80))
    friendphone = db.Column(db.String(80))
    status = db.Column(db.String(80))

    def __init__(self, phonedigits, friendname, friendphone, status):
        self.phonedigits = phonedigits
        self.friendname = friendname
        self.friendphone = friendphone
        self.status = status
#        self.num = num
    def json(self):
        return {'phonedigits': self.phonedigits, 'friendname': self.friendname, 'friendphone': self.friendphone, 'status': self.status}

    @classmethod
    #def find_by_measure(cls, name):
    def find_by_measure(cls, phonedigits):
       #return cls.query.filter_by(name=name).first()

       y = phonedigits.split("-")

       #return cls.query.filter_by(phonedigits=y[0], friendphone=y[1]).all()
       firstquery = cls.query.filter_by(phonedigits=y[0],friendphone=y[1]).first()
       #return cls.query.filter_by(phonedigits=phonedigits).first()
       return firstquery
       #return cls.query.filter_by(phonedigits=phonedigits).first()

    # def find_by_measures(cls, phonedigits):
    #     return cls.query.filter_by(phonedigits=phonedigits).first()
    # #    y = phonedigits.split("-")
    # #
    # #    return cls.query.filter_by(phonedigits=y[0], friendphone=y[1]).first()



    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
