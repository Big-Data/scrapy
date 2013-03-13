from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from viewStat.items import ViewstatItem
import unicodedata


class viewStatYoukuSpider(BaseSpider):
	name = "viewStatYouku"
	allowed_domains = ["http://i.youku.com/"]
	#'''
	start_urls = [
		"http://i.youku.com/u/UNDg2MzI4Nzgw/videos/order_1_view_1_page_1",
		"http://i.youku.com/u/UNDg2MzI4Nzgw/videos/order_1_view_1_page_2",
		"http://i.youku.com/u/UNDg2MzI4Nzgw/videos/order_1_view_1_page_3",
		"http://i.youku.com/u/UNDg2MzI4Nzgw/videos/order_1_view_1_page_4",
		"http://i.youku.com/u/UNDg2MzI4Nzgw/videos/order_1_view_1_page_5",
		"http://i.youku.com/u/UNDg2MzI4Nzgw/videos/order_1_view_1_page_6",
		"http://i.youku.com/u/UNDg2MzI4Nzgw/videos/order_1_view_1_page_7"	
	]
	#'''
	#start_urls = [
	#	"http://i.youku.com/u/UNDg2MzI4Nzgw/videos/order_1_view_1_page_3"
	#	]
	
	def parse(self, response):
	
	
		hxs =  HtmlXPathSelector(response)
		videoNameVec = hxs.select('//div[2]/div/div[2]/div/ul/li/a/text()').extract()
		videoViewNumVec = hxs.select('//ul/li/span[2]/text()').extract()
		videoLengthVec = hxs.select("//div[2]/div/ul/li[@class = 'v_time']/span[1]/text()").extract()
		videoUploadDateVec = hxs.select("//div[2]/div/ul/li[@class='v_pub']/span/text()").extract()
		# The format is 20941 characters from the CJK Unified Ideographs block.
	
		# Check if the length is the same
		numVN = len(videoNameVec)
		numVNV = len(videoViewNumVec)
	
		if (numVN != numVNV):
			print 'fetch failed'
	
		# if pass the test, continue to assign to structure
		videoItems = []
		for iVideo in range(numVN):
			item = ViewstatItem()
			item['name'] = videoNameVec[iVideo]
			item['viewNum'] = videoViewNumVec[iVideo]
			item['length'] = videoLengthVec[iVideo]
			item['uploadDate'] = videoUploadDateVec[iVideo]			
			videoItems.append(item)
			
			
		return videoItems
		
class viewStatTudouSpider(BaseSpider):
	name = "viewStatTudou"
	allowed_domains = ["http://i.youku.com/"]
	
	start_urls = [
		'http://www.tudou.com/home/item_u118852054s1p1.html',
		'http://www.tudou.com/home/item_u118852054s1p2.html',
		'http://www.tudou.com/home/item_u118852054s1p3.html'
	]
	
	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		videoNameVec = hxs.select('//div/div/div/div/h1/a/text()').extract()
		videoViewNumVec = hxs.select('//div[1]/div/div/div/div[2]/ul/li[3]').extract()
		videoLengthVec = hxs.select('//div[1]/div/div/div/div[2]/ul/li[1]').extract()
		videoUploadDateVec = hxs.select('//div[1]/div/div/div/div[2]/ul/li[2]').extract()
		
		numVideo = len(videoNameVec)
		
		videoItems = []
		
		for iVideo in range(numVideo):
			item = ViewstatItem()
			item['name'] = videoNameVec[iVideo]
			item['viewNum'] = videoViewNumVec[iVideo]			
			item['length'] = videoLengthVec[iVideo]
			item['uploadDate'] = videoUploadDateVec[iVideo]		
			videoItems.append(item)
			
		return videoItems