import requests
from parsel import Selector

from steamformatter import log
from steamformatter.parsers import USER_AGENT


def parse_reddit(url):
    # https://www.reddit.com/r/GameDeals/comments/6muj6q/bundle_stars_killer_bundle_x_499_469_529_the/dk5r1lg/
    op = '/comments/' not in url
    resp = requests.get(url, headers={'User-Agent': USER_AGENT})  # reddit is a cunt for scraping and their api sucks
    sel = Selector(text=resp.text)
    if op:
        steam_ids = sel.xpath("//form[contains(@id,'t3')][1]//a/@href[re:test(.,'steampowered.com/app/\d+')]")
    else:
        steam_ids = sel.xpath("//form[contains(@id,'t1')][1]//a/@href[re:test(.,'steampowered.com/app/\d+')]")
    steam_ids = steam_ids.re('app/(\d+)')
    log.info('downloading "{}" steam ids from reddit comment...'.format(len(steam_ids)))
    return steam_ids


