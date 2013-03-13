from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from proTrain.items import ProtrainItem

class indeedJobSpider(BaseSpider):
	name = "indeedJob"
	allowed_domains = ["indeed.com"]
	
	start_urls = [
		"http://www.indeed.com/q-java-entry-jobs.html",
		"http://www.indeed.com/q-c-entry-jobs.html",
		"http://www.indeed.com/q-python-entry-jobs.html",
		"http://www.indeed.com/q-php-entry-jobs.html",
		"http://www.indeed.com/q-perl-entry-jobs.html",
		"http://www.indeed.com/q-ruby-entry-jobs.html",
		"http://www.indeed.com/q-matlab-entry-jobs.html",
		"http://www.indeed.com/q-stata-entry-jobs.html",
		"http://www.indeed.com/q-sas-entry-jobs.html",
		"http://www.indeed.com/q-spss-entry-jobs.html"
		]
	'''
	# the format cannot handle c#
	start_urls = [
		"http://www.indeed.com/q-c%23-entry-jobs.html",
		]
	'''
	
	def parse(self, response):
		
		# parse the search name
		searchName = 'search';
		splitItems = response.url.split("-")
		print 'data is ', splitItems
		
		mainKey = splitItems[1]
		condition = splitItems[2:-1]
		
		hxs = HtmlXPathSelector(response)
		entries = hxs.select('//ul/li')
		
		# first process the value list
		valueCandidateObj = hxs.select('//ul/li/text()').extract()
		numPotentialValObj = len(valueCandidateObj)
		valList = [];
		for i in range(numPotentialValObj):
			if len(valueCandidateObj[i]) > 4:
				valList.append(valueCandidateObj[i][2:-3])
		
		numVal = len(valList)
		# construct the type obj
		typeObj = hxs.select('//ul/li/a/text()').extract()
		numType = len(typeObj)
		
		if numType != numVal:
			print 'number of type does not number of value, scrap failed'
		
		searchItems = []
		
		for iItem in range(numType):
			item = ProtrainItem()
			item['type'] = typeObj[iItem][1:-1]
			# process the entry value, it has unwanted (---)\n\n 
			item['value'] = valList[iItem]
			item['mainKey'] = mainKey
			item['condition'] = condition
			searchItems.append(item)
		return searchItems

		