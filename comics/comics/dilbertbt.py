from comics.aggregator.crawler import CrawlerBase
from comics.meta.base import MetaBase

class Meta(MetaBase):
    name = 'Dilbert (bt.no)'
    language = 'no'
    url = 'http://www.bt.no/tegneserier/dilbert/'
    start_date = '1989-04-16'
    rights = 'Scott Adams'

class Crawler(CrawlerBase):
    history_capable_date = '2005-10-28'
    time_zone = 1

    def crawl(self, pub_date):
        pass # Comic no longer published
