from datetime import datetime
import requests
from server import db, Ad, app

cur_year = datetime.now().strftime('%Y')
year_diff = 3
url = 'https://devman.org/assets/ads.json'


def get_or_create(session, model, adv_dict):
    instance = session.query(model).filter_by(id=adv_dict['id']).first()
    if instance:
        return instance, True
    else:
        instance = Ad()
        for key, value in adv_dict.items():
            if hasattr(instance, key):
                setattr(instance, key, value)
        session.add(instance)
        return instance, False


def inactive_olds(ads_ids):
    old_ads_ids = db.session.query(Ad).filter(Ad.id.notin_(ads_ids))
    for ad in old_ads_ids:
        ad.active = False


def update_db(data):
    for ad in json_data:
        row, exist = get_or_create(db.session, Ad, ad)
        if exist:
            for key, value in ad.items():
                if hasattr(row, key):
                    setattr(row, key, value)
        if (ad['under_construction'] or
                int(cur_year) - int(ad['construction_year'] or 0) < year_diff):
            row.new_building = True
        row.active = True


if __name__ == '__main__':
    json_data = requests.get(url).json()
    ads_ids = [ad['id'] for ad in json_data]
    with app.app_context():
        inactive_olds(ads_ids)
        update_db(json_data)
        db.session.commit()
