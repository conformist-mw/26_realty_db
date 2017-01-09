from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Ad(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    settlement = db.Column(db.String(30))
    under_construction = db.Column(db.Boolean)
    description = db.Column(db.Text)
    price = db.Column(db.Integer)
    oblast_district = db.Column(db.String(30))
    living_area = db.Column(db.Float)
    has_balcony = db.Column(db.Boolean)
    address = db.Column(db.String(30))
    construction_year = db.Column(db.String(5))
    rooms_number = db.Column(db.Integer)
    premise_area = db.Column(db.Float)
    active = db.Column(db.Boolean)
    new = db.Column(db.Boolean)

    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])
        # self.id = kwargs['id']
        # self.settlement = kwargs['settlement']
        # self.under_construction = kwargs['under_construction']
        # self.description = kwargs['description']
        # self.price = kwargs['price']
        # self.oblast_district = kwargs['oblast_district']
        # self.living_area = kwargs['living_area']
        # self.has_balcony = kwargs['has_balcony']
        # self.address = kwargs['address']
        # self.construction_year = kwargs['construction_year']
        # self.rooms_number = kwargs['rooms_number']
        # self.premise_area = kwargs['premise_area']
        # self.active = kwargs['active']
        # self.new = kwargs['new']
