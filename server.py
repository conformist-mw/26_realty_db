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
@app.route('/<int:page>', methods=['GET'])
def ads_list(page=1):
    ads = Ad.query.order_by(Ad.price).paginate(page, 10)
    return render_template('ads_list.html', ads=ads)


@app.route('/search', methods=['POST'])
@app.route('/search/<int:page>', methods=['GET', 'POST'])
def search(page=1):
    max_num = db.session.query(func.max(Ad.price)).one()[0]
    new_building = request.form.get('new_building', False, type=bool)
    oblast_district = request.form['oblast_district']
    min_price = request.form.get('min_price', 0, type=int)
    max_price = request.form.get('max_price', max_num, type=int)
    ads = Ad.query.filter(
        Ad.oblast_district == oblast_district,
        Ad.new_building.is_(new_building),
        Ad.price > min_price, Ad.price < max_price,
        Ad.active.is_(True)).order_by(Ad.price).paginate(page, 10)
    return render_template('ads_list.html', ads=ads)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
