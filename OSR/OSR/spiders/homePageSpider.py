from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.shell import inspect_response


from OSR.items import videoItem


import unicodedata

class youkuHomePageSpider(BaseSpider):
	name = "youku"
	allowed_domains = ["http://i.youku.com/"]
	
	start_urls = [
		"http://i.youku.com/u/UNDg2MzI4Nzgw/videos/order_1_view_1_page_1",
		"http://i.youku.com/u/UNDg2MzI4Nzgw/videos/order_1_view_1_page_2",
		"http://i.youku.com/u/UNDg2MzI4Nzgw/videos/order_1_view_1_page_3",
		"http://i.youku.com/u/UNDg2MzI4Nzgw/videos/order_1_view_1_page_4",
		"http://i.youku.com/u/UNDg2MzI4Nzgw/videos/order_1_view_1_page_5",
		"http://i.youku.com/u/UNDg2MzI4Nzgw/videos/order_1_view_1_page_6",
		"http://i.youku.com/u/UNDg2MzI4Nzgw/videos/order_1_view_1_page_7",
		"http://i.youku.com/u/UNDg2MzI4Nzgw/videos/order_1_view_1_page_8",
		"http://i.youku.com/u/UNDg2MzI4Nzgw/videos/order_1_view_1_page_9"
	]
	'''
	start_urls = [
		"http://i.youku.com/u/UNDg2MzI4Nzgw/videos/order_1_view_1_page_1"
		]
	'''	
	metaList = []
	
	def parse(self, response):
	
		#inspect_response(response)
		
		hxs =  HtmlXPathSelector(response)
		videoNameVec = hxs.select('//div[2]/div/div[2]/div/ul/li/a/text()').extract()
		videoViewNumVec = hxs.select('//ul/li/span[2]/text()').extract()
		videoPubTimeVec = hxs.select('//div[2]/div/ul/li[@class = "v_pub"]/span/text()').extract()
		# The format is 20941 characters from the CJK Unified Ideographs block.
	
		# Check if the length is the same
		numVN = len(videoNameVec)
		numVNV = len(videoViewNumVec)
		numPTV = len(videoViewNumVec)
	
		if (numVN != numVNV) or (numVN != numPTV):
			raise NameError( 'fetch failed for youku' )
	
		# if pass the test, continue to assign to structure
		itemList = []
		for iVideo in range(numVN):
			item = videoItem()
			item['name'] = videoNameVec[iVideo]
			item['viewNum'] = videoViewNumVec[iVideo]
			item['pubTime'] = videoPubTimeVec[iVideo]
			itemList.append(item)

		return	itemList
		

class tudouHomePageSpider(BaseSpider):

    name = "tudou"
    allowed_domains = ["http://www.tudou.com/"]
	
    start_urls = [
		"http://www.tudou.com/home/item_u118852054s0p1.html",
		"http://www.tudou.com/home/item_u118852054s0p2.html",
		"http://www.tudou.com/home/item_u118852054s0p3.html",
		"http://www.tudou.com/home/item_u118852054s0p4.html"
    ]
	
    def parse(self, response):
		hxs =  HtmlXPathSelector(response)
		
		videoNameVec = hxs.select('//div/div/div/div/h1/a/text()').extract()
		videoViewNumVec = hxs.select('//ul[@class = "info"]/li[3]/text()').extract()
		videoPubTimeVec = hxs.select('//ul[@class = "info"]/li[2]/text()').extract()		
		videoLengthVec = hxs.select('//ul[@class = "info"]/li[1]/text()').extract()
		
		# check for errors
		numVN = len(videoNameVec)
		numVNV = len(videoViewNumVec)
		numPTV = len(videoViewNumVec)
		numLV = len(videoLengthVec)
	
		if (numVN != numVNV) or (numVN != numPTV) or (numVN != numLV):
			raise NameError( 'fetch failed for tudou' )
	
		# if pass the test, continue to assign to structure
		itemList = []
		for iVideo in range(numVN):
			item = videoItem()
			item['name'] = videoNameVec[iVideo]
			item['viewNum'] = videoViewNumVec[iVideo]
			item['pubTime'] = videoPubTimeVec[iVideo]
			item['length'] = videoLengthVec[iVideo]
			itemList.append(item)
		return	itemList	

