from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from degreeMill.items import collegeItem, resumeItem
from degreeMill.spiders.resumeSpider import resumeSpider
from scrapy.http.request import Request
from scrapy.shell import inspect_response


class collegeSpier(BaseSpider):
	name = "college"
	allowed_domains = ["indeed.com"]
	
	start_urls = [
		'http://www.indeed.com/resumes?q=school%3A("Abet+International+University")',
		'http://www.indeed.com/resumes?q=school%3A("Almeda+University")',
		'http://www.indeed.com/resumes?q=school%3A("American+Capital+University")',		
		'http://www.indeed.com/resumes?q=school%3A("American+Global+International+University")',
		'http://www.indeed.com/resumes?q=school%3A("Amstead+University")',		
		'http://www.indeed.com/resumes?q=school%3A("Ashwood+University")',			
		'http://www.indeed.com/resumes?q=school%3A("Atlantic+International+University")',
		'http://www.indeed.com/resumes?q=school%3A("barrington++University")',
		'http://www.indeed.com/resumes?q=school%3A("Belford+University")',
		'http://www.indeed.com/resumes?q=school%3A("Bienville+University")',		
		'http://www.indeed.com/resumes?q=school%3A("Breyer+State+University")',
		'http://www.indeed.com/resumes?q=school%3A("Bronte+International+University")',
		'http://www.indeed.com/resumes?q=school%3A("Cambell+State+University")',
		'http://www.indeed.com/resumes?q=school%3A("Canyon+University")',
		'http://www.indeed.com/resumes?q=school%3A("Central+State+University+of+New+York")',
		'http://www.indeed.com/resumes?q=school%3A("Century+University")',
		'http://www.indeed.com/resumes?q=school%3A("Clayton+College+of+Natural+Health")'
		]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		
		# build the resume spider
		testSpider = resumeSpider();
		
		
		# select the resumes
		resumeUnicode = hxs.select("//li/div/div/a/@href").extract()
		
		if len(resumeUnicode) == 0:
			print 'The following URL returns Null Result'
			print response.url
			# end the function callback
			return
		
		# spider all the resume 
		#print 'start scraping'
		for iResume in resumeUnicode:
			# make the url
			resumeUrl = "http://www.indeed.com" + iResume.encode('ascii')	
			#print resumeUrl
			yield Request(resumeUrl, callback = testSpider.parse)

		
		
		# find the next url link
		nextLinkUni = hxs.select('//div[3]/div[2]/a[@class = "instl next"]/@href').extract()
		nextLinkTrue = len(nextLinkUni)
		
		if nextLinkTrue == 1:
			#print 'go next link'
			nextLinkUrl = "http://www.indeed.com/resumes" + nextLinkUni[0].encode('ascii')
			yield Request(nextLinkUrl, callback = self.parse)
		elif nextLinkTrue == 0:
			print 'search end'
		#return searchResult
		

