import json

import requests
from parsel import Selector

from steamformatter import log

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'


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


def scrape_bundlestars_bundle(url):
    response = requests.get(url)
    data = json.loads(response.text)
    games = data['bundles'][0]['games']
    for steam_id in [g['steam']['id'] for g in games]:
        yield steam_id


def scrape_reddit(url, op=False):
    resp = requests.get(url, headers={'User-Agent': USER_AGENT})  # reddit is a cunt for scraping and their api sucks
    sel = Selector(text=resp.text)
    if op:
        steam_ids = sel.xpath("//form[contains(@id,'t3')][1]//a/@href[re:test(.,'steampowered.com/app/\d+')]")
    else:
        steam_ids = sel.xpath("//form[contains(@id,'t1')][1]//a/@href[re:test(.,'steampowered.com/app/\d+')]")
    steam_ids = steam_ids.re('app/(\d+)')
    log.info('downloading "{}" steam ids from reddit comment...'.format(len(steam_ids)))
    return steam_ids


def scrape_steam(response):
    sel = Selector(text=response.text)
    rating = sel.css("span.responsive_reviewdesc").re('\d+%')
    tags = sel.css("#game_highlights .app_tag::text").extract()[:3]
    name = sel.css('.apphub_AppName::text').extract_first()
    return {
        'name': name,
        'rating': rating[-1] if rating else '~',
        'tags': ','.join([t.strip() for t in tags if t.strip() != '+']),
        'steam_url': response.url,
    }


