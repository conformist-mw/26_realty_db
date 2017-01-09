import json
from urllib.request import urlopen
from server import db, Ad, create_app

current_year = 2017
url = 'https://devman.org/assets/ads.json'


def get_or_create(session, model, adv_dict):
    instance = session.query(model).filter_by(id=adv_dict['id']).first()
    if instance:
        return instance, True
    else:
        instance = Ad(**adv_dict)
        session.add(instance)
        return instance, False


def get_json(url):
    page = urlopen(url)
    page_data = page.read().decode('utf-8')
    return json.loads(page_data)


json_data = get_json(url)
ads_ids = [ad['id'] for ad in json_data]

app = create_app()
ctx = app.app_context()
ctx.push()
old_ads_ids = db.session.query(Ad).filter(Ad.id.notin_(ads_ids))

for ad in old_ads_ids:
    ad.active = False

for ad in json_data:
    row, exist = get_or_create(db.session, Ad, ad)
    if exist:
        for key, value in ad.items():
            setattr(row, key, value)
    if (ad['under_construction'] or
            current_year - int(ad['construction_year'] or 0) < 3):
        row.new = True
    row.active = True
db.session.commit()
ctx.pop()
