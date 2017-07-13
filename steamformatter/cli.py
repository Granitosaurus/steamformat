from urllib.parse import urlparse

import click
import logging

from steamformatter import log
from steamformatter.aiocrawler import download_urls
from steamformatter.output import format_comment
from steamformatter.parsers import parse_bundlestars_bundle, parse_reddit, parse_steam, SteamItem

PARSERS = {
    'bundlestars.com': parse_bundlestars_bundle,
    'reddit.com': parse_reddit,
}


@click.command()
@click.argument('url')
@click.option('--nolog', is_flag=True, help="produce no log")
@click.option('--sort', type=click.Choice(SteamItem._fields), help="sort fields", show_default=True, default='rating')
def cli(url, nolog, sort):
    if nolog:
        log.setLevel(logging.CRITICAL)
    parsed_url = urlparse(url)
    parser = PARSERS.get(parsed_url.netloc.replace('www.', ''))
    if not parser:
        print('no parser found for {}'.format(parsed_url.netloc))
        return
    steam_ids = parser(url)
    urls = [f"http://store.steampowered.com/app/{i}" for i in steam_ids]
    log.info('downloading game data from steam...')
    items = [parse_steam(resp) for resp in download_urls(urls)]
    print(format_comment(items, sort=sort))

if __name__ == '__main__':
    cli()
