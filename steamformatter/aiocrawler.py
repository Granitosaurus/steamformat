import asyncio
from collections import namedtuple

import async_timeout
from aiohttp import ClientSession

Response = namedtuple('Response', ['url', 'text'])


class AioCrawler:
    """
    Asynchronious crawler using aiohttp package
    """

    async def fetch(self, url, session):
        """Asynchroniously retrieve url as wappy.Response object"""
        with async_timeout.timeout(10):
            async with session.get(url) as response:
                print(f'downloading: {url}')
                text = await response.text()
                return Response(response.url, text)

    async def fetch_urls(self, urls):
        """Fetch mutliple urls"""
        tasks = []
        async with ClientSession() as session:
            for url in urls:
                task = asyncio.ensure_future(self.fetch(url, session))
                tasks.append(task)
            responses = asyncio.gather(*tasks, return_exceptions=True)
            return await responses

    def download_urls(self, urls):
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(self.fetch_urls(urls))
        responses = loop.run_until_complete(future)
        return [r for r in responses if isinstance(r, Response)]
