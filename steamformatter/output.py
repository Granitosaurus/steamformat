from steamformatter import log
import re


def format_comment(items, sort=None):
    if not sort:
        sort = 'rating'
    # todo sorting
    log.info('formatting data:\n')
    header = [
        '| Name   | Rating     | Tags   |',
        '|:-------|:----------:|:-------|'
    ]
    lines = []
    items = sorted(items, key=lambda v: v._asdict()[sort], reverse=True)
    for item in items:
        lines.append('|[{name}]({steam_url})  | {rating}  | {tags}  |'.format(**item._asdict()))
    return '  \n'.join(header + lines)


