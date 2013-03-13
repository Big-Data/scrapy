from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from proTrain.items import ProtrainItem

class indeedCondJobSpider(BaseSpider):
	name = "indeedCondJob"
	allowed_domains = ["indeed.com"]
	
	start_urls = [
		"http://www.indeed.com/q-java-entry-years-experience-jobs.html",
		"http://www.indeed.com/q-c-entry-years-experience-jobs.html",
		"http://www.indeed.com/q-python-entry-years-experience-jobs.html",
		"http://www.indeed.com/q-php-entry-years-experience-jobs.html",
		"http://www.indeed.com/q-perl-entry-years-experience-jobs.html",
		"http://www.indeed.com/q-ruby-entry-years-experience-jobs.html",
		"http://www.indeed.com/q-matlab-entry-years-experience-jobs.html",
		"http://www.indeed.com/q-stata-entry-years-experience-jobs.html",
		"http://www.indeed.com/q-sas-entry-years-experience-jobs.html",
		"http://www.indeed.com/q-spss-entry-years-experience-jobs.html",
		]
	'''
	start_urls = [
		"http://www.indeed.com/q-java-entry-years-experience-jobs.html",
		]
	'''
	def parse(self, response):
		
		# parse the search name
		searchName = 'search';
		splitItems = response.url.split("-")
		
		mainKey = splitItems[1]
		condition = splitItems[2:-1]
		print mainKey, condition
		#open(filename, 'wb').write(response.body)
		
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

		