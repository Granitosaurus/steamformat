from collections import namedtuple

from requests_futures.sessions import FuturesSession

from steamformatter import log

Response = namedtuple('Response', ['url', 'text'])


def _get_response(future):
    try:
        response = future.result()
        log.debug(f'downloaded: {response.url}')
        return response
    except Exception as e:
        log.debug(f'Failure: {e}')


def download_urls(urls):
    with FuturesSession(max_workers=1) as session:
        futures = [session.get(url, timeout=10, cookies={'mature_content': '1'}) for url in urls]
        for f in futures:
            response = _get_response(f)
            if not response:
                continue
            yield response

