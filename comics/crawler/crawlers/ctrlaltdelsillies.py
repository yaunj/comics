from comics.crawler.base import BaseComicCrawler
from comics.crawler.meta import BaseComicMeta

class ComicMeta(BaseComicMeta):
    name = 'Ctrl+Alt+Del Sillies'
    language = 'en'
    url = 'http://www.ctrlaltdel-online.com/'
    start_date = '2008-06-27'
    history_capable_date = '2008-06-27'
    schedule = 'Mo,Tu,We,Th,Fr,Sa,Su'
    time_zone = -5
    rights = 'Tim Buckley'

class ComicCrawler(BaseComicCrawler):
    def _get_url(self):
        self.url = 'http://www.cad-comic.com/comics/Lite%(date)s.jpg' % {
            'date': self.pub_date.strftime('%Y%m%d'),
        }
