from flask import Flask, render_template
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


if __name__ == "__main__":
    app.run(host='0.0.0.0')
