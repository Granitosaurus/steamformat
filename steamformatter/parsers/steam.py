from collections import namedtuple

from parsel import Selector

SteamItem = namedtuple('SteamItem', ['name', 'rating', 'tags', 'steam_url'])


def parse_steam(response):
    sel = Selector(text=response.text)
    rating = sel.css("span.responsive_reviewdesc").re('\d+%')
    tags = sel.css("#game_highlights .app_tag::text").extract()[:3]
    name = sel.css('.apphub_AppName::text').extract_first()
    data = {
        'name': name,
        'rating': rating[-1] if rating else '~',
        'tags': ','.join([t.strip() for t in tags if t.strip() != '+']),
        'steam_url': response.url,
    }
    return SteamItem(**data)
