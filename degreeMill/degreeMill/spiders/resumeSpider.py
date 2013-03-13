from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from degreeMill.items import resumeItem
from scrapy.shell import inspect_response
import json
import unicodedata

class resumeSpider(BaseSpider):
	name = "resume"
	allowed_domains = ["indeed.com"]
	
	def parse(self, response):
				
		item = resumeItem()
		hxs = HtmlXPathSelector(response)
		

		# find the name
		item['name'] = hxs.select('//h1/text()').extract()
		# find all the  jobs
		item['jobTime'] = hxs.select('//div[1]/div[2]/div[2]/div[2]/div/div/p[@class = "work_dates"]/text()').extract()
	    # find all the educs
		item['eduTitle'] = hxs.select('//div[3]/div[2]/div/div/p[@class = "edu_title"]/text()').extract()
		#return resumeRecord
		item['eduDates'] = hxs.select('//div[3]/div[2]/div/div/p[@class = "edu_dates"]/text()').extract()
		item['eduSchool'] = hxs.select('//div[3]/div[2]/div/div/div/span/text()').extract()
		
		
		
		#inspect_response(response)
		
		# write it out
		nameStringList = item['name']
		nameString = nameStringList[0].encode('ascii','ignore')
		
		fileStr = 'resumeDump/' + nameString + '.json'
		fileId = open(fileStr,'w')
		line = json.dumps(dict(item)) + "\n"
		fileId.write(line)
		