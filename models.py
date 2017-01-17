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
    active = db.Column(db.Boolean, default=True)
    new_building = db.Column(db.Boolean, default=False)
