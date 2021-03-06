# encoding: utf-8

from comics.aggregator.crawler import CrawlerBase, CrawlerImage
from comics.meta.base import MetaBase

class Meta(MetaBase):
    name = 'Butternutsquash'
    language = 'en'
    url = 'http://www.butternutsquash.net/'
    rights = 'Ramón Pérez & Rob Coughler'

class Crawler(CrawlerBase):
    start_date = '2003-04-16'
    history_capable_date = '2003-04-16'

    def crawl(self, pub_date):
        url = ('http://www.butternutsquash.net/v3/comics/'
            '%s-butternutsquash.jpg' % (pub_date.strftime('%Y-%m-%d'),))
        return CrawlerImage(url)
