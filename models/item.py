from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    num = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    phonenumber = db.Column(db.String(80))
    name = db.Column(db.String(80))

    def __init__(self, name, phonenumber, latitude, longitude):
        self.name = name
        self.phonenumber = phonenumber
        self.latitude = latitude
        self.longitude = longitude
#        self.num = num
    def json(self):
        return {'name': self.name, 'phonenumber': self.phonenumber, 'latitude': self.latitude, 'longitude': self.longitude}

    @classmethod
    #def find_by_measure(cls, name):
    def find_by_measure(cls, phonenumber)
       #return cls.query.filter_by(name=name).first()
       return cls.query.filter_by(phonenumber=phonenumber).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
