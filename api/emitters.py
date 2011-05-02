from piston.emitters import Emitter
import PyRSS2Gen
import datetime

class RSSEmitter(Emitter):


	def render(self, request):
		
		data = self.construct()
		rss_items = []
		for item in data:
			rss_items.append(PyRSS2Gen.RSSItem(
					title = item['title'],
					description = item['synopsis'],
					link = item['url'],
					pubDate = item['date_created'],
				))
			
	
		rss = PyRSS2Gen.RSS2(
			title = "RSS for Something",
			link = "http://news.something.com",
			description = "Test",
			lastBuildDate = datetime.datetime.utcnow(),
			items = rss_items			
		)
		
		
		return rss.to_xml(encoding="utf-8")
		#return data
	
# Register Emitter
Emitter.register('rss', RSSEmitter, 'charset=utf-8')
