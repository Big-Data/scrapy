from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from youkuData.items import YoukuVideoItem
import unicodedata

class youkuIndexSpider(BaseSpider):
    name = "youkuIndexSpider"
    allowed_domains = ["index.youku.html"]
	
    start_urls = [
		
	]
	
    def parse(self, response):
	
		# try to hit it to see if we still get the error
        print response
		
class youkuHomePageSpider(BaseSpider):
	name = "youkuHomePage"
	allowed_domains = ["http://i.youku.com/"]
	
	start_urls = [
		"http://i.youku.com/u/UNDg2MzI4Nzgw/videos/order_1_view_1_page_1",
		"http://i.youku.com/u/UNDg2MzI4Nzgw/videos/order_1_view_1_page_2",
		"http://i.youku.com/u/UNDg2MzI4Nzgw/videos/order_1_view_1_page_3",
		"http://i.youku.com/u/UNDg2MzI4Nzgw/videos/order_1_view_1_page_4",
		"http://i.youku.com/u/UNDg2MzI4Nzgw/videos/order_1_view_1_page_5",
		"http://i.youku.com/u/UNDg2MzI4Nzgw/videos/order_1_view_1_page_6",
		"http://i.youku.com/u/UNDg2MzI4Nzgw/videos/order_1_view_1_page_7"	
	]
	'''
	start_urls = [
		"http://i.youku.com/u/UNDg2MzI4Nzgw/videos/order_1_view_1_page_1"
		]
	'''
	def parse(self, response):
	
		hxs =  HtmlXPathSelector(response)
		videoNameVec = hxs.select('//div[2]/div/div[2]/div/ul/li/a/text()').extract()
		videoViewNumVec = hxs.select('//ul/li/span[2]/text()').extract()
		# The format is 20941 characters from the CJK Unified Ideographs block.
	
		# Check if the length is the same
		numVN = len(videoNameVec)
		numVNV = len(videoViewNumVec)
	
		if (numVN != numVNV):
			print 'fetch failed'
	
		# if pass the test, continue to assign to structure
		videoItems = []
		for iVideo in range(numVN):
			item = YoukuVideoItem()
			item['name'] = videoNameVec[iVideo]
			item['viewNum'] = videoViewNumVec[iVideo]
			videoItems.append(item)
			
			
		return videoItems