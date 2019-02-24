from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    num = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    name = db.Column(db.String(80))

    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
#        self.num = num
    def json(self):
        return {'name': self.name, 'latitude': self.latitude, 'longitude': self.longitude}

    @classmethod
    def find_by_measure(cls, name):
       return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
