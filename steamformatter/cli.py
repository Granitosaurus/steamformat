import click
import logging

from steamformatter import log
from steamformatter.aiocrawler import AioCrawler
from steamformatter.output import format_comment
from steamformatter.scrape import scrape_bundlestars_bundle, scrape_reddit, scrape_steam


@click.command()
@click.argument('url')
@click.option('--selfpost', is_flag=True,
              help="extract from self post instead")
@click.option('--bundlestars', is_flag=True,
              help="scrape from bundlestars")
@click.option('--nolog', is_flag=True,
              help="produce no log")
def cli(url, bundlestars, nolog, selfpost):
    if nolog:
        log.setLevel(logging.CRITICAL)
    if bundlestars:
        steam_ids = scrape_bundlestars_bundle(url)
    else:
        steam_ids = scrape_reddit(url, selfpost)
    urls = [f"http://store.steampowered.com/app/{i}" for i in steam_ids]
    log.info('downloading game data from steam...')
    crawler = AioCrawler()
    data = crawler.download_urls(urls)
    items = []
    for resp in data:
        items.append(scrape_steam(resp))
    print(format_comment(items))


if __name__ == '__main__':
    cli()