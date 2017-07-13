from steamformatter import log
import re


def format_comment(items, sort='rating'):
    # todo sorting
    log.info('formatting data:\n')
    header = [
        '| Name   | Rating     | Tags   |',
        '|:-------|:----------:|:-------|'
    ]
    lines = []
    for item in items:
        lines.append('|[{name}]({steam_url})  | {rating}  | {tags}  |'.format(**item))
    lines = sorted(lines, key=lambda v: int((re.findall('(\d+)%', v) or [0])[0]), reverse=True)
    return '  \n'.join(header + lines)


