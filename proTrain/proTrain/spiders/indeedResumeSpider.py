from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from proTrain.items import ProtrainItem


class indeedResumeSpider(BaseSpider):
	name = "indeedResume"
	allowed_domains = ["indeed.com"]
	start_urls = [
		"http://www.indeed.com/resumes?q=java",
		"http://www.indeed.com/resumes?q=c",
		"http://www.indeed.com/resumes?q=c%23",
		"http://www.indeed.com/resumes?q=python",
		"http://www.indeed.com/resumes?q=php",
		"http://www.indeed.com/resumes?q=perl",
		"http://www.indeed.com/resumes?q=ruby",
		"http://www.indeed.com/resumes?q=matlab",
		"http://www.indeed.com/resumes?q=stata",
		"http://www.indeed.com/resumes?q=sas",
		"http://www.indeed.com/resumes?q=spss"
	]
	
	def parse(self, response):
	
		splitItems = response.url.split("=")
		mainKey = splitItems[-1]

		hxs = HtmlXPathSelector(response)
		# the following code hinges on the assumption that typeObj and ValObj would have same length
		# thus a 1-1 mapping
		typeObj = hxs.select('//ul/li/a/text()').extract()
		valObj = hxs.select('//ul/li/span/text()').extract()
	
		numObj = len(typeObj)
		if numObj != len(valObj):
			print 'the length of the type obj and value obj does not match. Scrap failed.'
		
		searchItems = []
		for iObj in range(numObj):
			if typeObj[iObj] == 'Less than 1 year' or typeObj[iObj] == '1-2 years':
				item = ProtrainItem()
				item['type'] = typeObj[iObj]
				item['value'] = valObj[iObj][0:-1]
				item['mainKey'] = mainKey
				searchItems.append(item)			
		return searchItems