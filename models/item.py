from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    magnitude = db.Column(db.Float(precision=1))
    name = db.Column(db.String(80))

    def __init__(self, name, magnitude):
        self.name = name
        self.magnitude = magnitude

    def json(self):
        return {'name': self.name, 'magnitude': self.magnitude}

    @classmethod
    def find_by_measure(cls, name):
       return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
