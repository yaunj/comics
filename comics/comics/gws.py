from comics.aggregator.crawler import CrawlerBase, CrawlerImage
from comics.meta.base import MetaBase

class Meta(MetaBase):
    name = 'Girls With Slingshots'
    language = 'en'
    url = 'http://www.girlswithslingshots.com/'
    start_date = '2004-09-30'
    rights = 'Danielle Corsetto'

class Crawler(CrawlerBase):
    history_capable_days = 1
    schedule = 'Mo,Tu,We,Th,Fr'
    time_zone = -5

    def crawl(self, pub_date):
        page = self.parse_page('http://www.daniellecorsetto.com/gws.html')
        url = page.src(
            'img[src^="http://www.daniellecorsetto.com/images/gws/GWS"]')
        return CrawlerImage(url)
