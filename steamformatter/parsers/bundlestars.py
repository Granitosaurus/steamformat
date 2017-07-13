import json

import re
import requests

API_URL = 'https://www.bundlestars.com/api/products/'


def parse_bundlestars_bundle(url):
    if 'api/products' not in url:
        product = re.findall('(?:products|bundle)/([^/]+)', url)
        if not product:
            return
        url = API_URL + product[0]
    response = requests.get(url)
    data = json.loads(response.text)
    games = data['bundles'][0]['games']
    for steam_id in [g['steam']['id'] for g in games]:
        yield steam_id

# def scrape_bundlestars(url):
#     data = requests.get(url)
#     print(json.loads(data.text))
#     products = json.loads(data.text)[0]['products']
#     urls = [f'https://www.bundlestars.com/api/products/{p["slug"]}' for p in products]
#     log.info('downloading "{}" steam ids from bundlestars bundle...'.format(len(urls)))
#     responses = a_download(urls)
#     for r in responses:
#         product = json.loads(r.text)
#         yield product['steam']['id']
