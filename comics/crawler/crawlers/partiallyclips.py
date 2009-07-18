from comics.crawler.base import BaseComicCrawler
from comics.crawler.meta import BaseComicMeta

class ComicMeta(BaseComicMeta):
    name = 'PartiallyClips'
    language = 'en'
    url = 'http://www.partiallyclips.com/'
    start_date = '2002-01-01'
    history_capable_days = 10
    schedule = 'Tu'
    time_zone = -5
    rights = 'Robert T. Balder'

class ComicCrawler(BaseComicCrawler):
    def _get_url(self):
        self.parse_feed('http://www.partiallyclips.com/includes/rss.xml')

        for entry in self.feed.entries:
            if self.timestamp_to_date(entry.updated_parsed) == self.pub_date:
                self.title = entry.title.split(' - ')[0]
                pieces = entry.summary.split('"')
                for i, piece in enumerate(pieces):
                    if piece.count('src='):
                        self.url = pieces[i + 1]
                        return
