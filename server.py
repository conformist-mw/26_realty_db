from flask import Flask, render_template, request
from sqlalchemy.sql import func
from models import db, Ad


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)
    return app


app = create_app()


@app.route('/')
def ads_list():
    return render_template('ads_list.html', ads=[{
        "settlement": "Череповец",
        "under_construction": False,
        "description": '''Квартира в отличном состоянии. Заезжай и живи!''',
        "price": 2080000,
        "oblast_district": "Череповецкий район",
        "living_area": 17.3,
        "has_balcony": True,
        "address": "Юбилейная",
        "construction_year": 2001,
        "rooms_number": 2,
        "premise_area": 43.0,
    }] * 10
    )


@app.route('/search', methods=['POST'])
def search():
    max_num = db.session.query(func.max(Ad.price)).one()[0]
    new_building = request.form.get('new_building', False)
    oblast_district = request.form['oblast_district']
    min_price = request.form.get('min_price', 0, type=int)
    max_price = request.form.get('max_price', max_num, type=int)
    ans = db.session.query(Ad).filter(
        Ad.oblast_district == oblast_district,
        Ad.new_building.is_(bool(new_building)),
        Ad.price > min_price, Ad.price < max_price).all()
    return render_template('ads_list.html', ads=ans)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
