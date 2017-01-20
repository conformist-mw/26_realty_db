from os import getenv
from flask import Flask, render_template, request, session, redirect, url_for
from sqlalchemy.sql import func
from models import db, Ad

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = getenv('SECRET')
db.init_app(app)
per_page = 10


@app.route('/')
@app.route('/<int:page>', methods=['GET'])
def ads_list(page=1):
    ads = Ad.query.order_by(Ad.price).paginate(page, per_page)
    return render_template('ads_list.html', ads=ads)


@app.route('/search', methods=['POST'])
def search(page=1):
    max_num = db.session.query(func.max(Ad.price)).one()[0]
    session['dist'] = request.form['oblast_district']
    session['minv'] = request.form.get('min_price', 0, type=int)
    session['maxv'] = request.form.get('max_price', max_num, type=int)
    session['new'] = request.form.get('new_building', False, type=bool)
    return redirect(url_for('results'))


@app.route('/results', methods=['GET'])
@app.route('/results/<int:page>', methods=['GET'])
def results(page=1):
    ads = Ad.query.filter(
        Ad.oblast_district == session['dist'],
        Ad.new_building.is_(session['new']),
        Ad.price > session['minv'], Ad.price < session['maxv'],
        Ad.active.is_(True)).order_by(Ad.price).paginate(page, per_page, False)
    return render_template('ads_list.html', ads=ads)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
