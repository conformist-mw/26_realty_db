import json
from urllib.request import urlopen
from server import db, Ad, create_app

url = 'https://devman.org/assets/ads.json'
page = urlopen(url)
page_data = page.read().decode('utf-8')
json_data = json.loads(page_data)

app = create_app()
ctx = app.app_context()
ctx.push()
for ad in json_data:
    new_ad = Ad(**ad)
    db.session.add(new_ad)
    db.session.commit()
ctx.pop()

