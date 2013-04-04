from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from degreeMill.items import collegeItem, resumeItem
from degreeMill.spiders.resumeSpider import resumeSpider
from scrapy.http.request import Request
from scrapy.shell import inspect_response


class collegeSpier(BaseSpider):
	name = "college"
	allowed_domains = ["indeed.com"]
	
	
	'''
	State Warning Issued
	
	start_urls = [
		'http://www.indeed.com/resumes?q=school%3A("Almeda+University")',
		'http://www.indeed.com/resumes?q=school%3A("American+Capital+University")',		
		'http://www.indeed.com/resumes?q=school%3A("Amstead+University")',		
		'http://www.indeed.com/resumes?q=school%3A("Ashwood+University")',			
		'http://www.indeed.com/resumes?q=school%3A("Atlantic+International+University")',
		'http://www.indeed.com/resumes?q=school%3A("barrington++University")',
		'http://www.indeed.com/resumes?q=school%3A("Belford+University")',
		'http://www.indeed.com/resumes?q=school%3A("Bienville+University")',		
		'http://www.indeed.com/resumes?q=school%3A("Breyer+State+University")',
		'http://www.indeed.com/resumes?q=school%3A("Bronte+International+University")',
		'http://www.indeed.com/resumes?q=school%3A("Canyon+University")',
		'http://www.indeed.com/resumes?q=school%3A("Century+University")',
		'http://www.indeed.com/resumes?q=school%3A("Clayton+College+of+Natural+Health")',
		'http://www.indeed.com/resumes?q=school%3A("Chadwick+University")',
		'http://www.indeed.com/resumes?q=school%3A("Columbia+Pacific+University")',
		'http://www.indeed.com/resumes?q=school%3A("Concordia+College")',		
		'http://www.indeed.com/resumes?q=school%3A("Corllins+University")',
		'http://www.indeed.com/resumes?q=school%3A("Hartford+University")',
		'http://www.indeed.com/resumes?q=school%3A("InterAmerican+University")',
		'http://www.indeed.com/resumes?q=school%3A("Kennedy+Western+University")',
		'http://www.indeed.com/resumes?q=school%3A("Lacrosse+University")',
		'http://www.indeed.com/resumes?q=school%3A("LaSalle+University")',
		'http://www.indeed.com/resumes?q=school%3A("Madison+University")',
		'http://www.indeed.com/resumes?q=school%3A("Miami+Christian+University")',
		'http://www.indeed.com/resumes?q=school%3A("Must+University")',
		'http://www.indeed.com/resumes?q=school%3A("Newport+University")',
		'http://www.indeed.com/resumes?q=school%3A("Novus+University")',
		'http://www.indeed.com/resumes?q=school%3A("Preston+University")',
		'http://www.indeed.com/resumes?q=school%3A("Randford+University")',
		'http://www.indeed.com/resumes?q=school%3A("Redding+University")',
		'http://www.indeed.com/resumes?q=school%3A("Richardson+University")',
		'http://www.indeed.com/resumes?q=school%3A("Rochville+University")',
		'http://www.indeed.com/resumes?q=school%3A("Rushmore+University")',
		'http://www.indeed.com/resumes?q=school%3A("Rutherford+University")',
		'http://www.indeed.com/resumes?q=school%3A("Sacramento+International+University")',
		'http://www.indeed.com/resumes?q=school%3A("Saint+Augustine+School+Medical+Assistants")',
		'http://www.indeed.com/resumes?q=school%3A("Saint+Regis+University")',
		'http://www.indeed.com/resumes?q=school%3A("San+Francisco+International+University")',
		'http://www.indeed.com/resumes?q=school%3A("Suffield+University")',
		'http://www.indeed.com/resumes?q=school%3A("Summit+University")',
		'http://www.indeed.com/resumes?q=school%3A("Stauron+University")',		
		'http://www.indeed.com/resumes?q=school%3A("Trinity+College+Natural+Health")',	
		'http://www.indeed.com/resumes?q=school%3A("Trinity+Southern+University")',	
		'http://www.indeed.com/resumes?q=school%3A("University+of+Berkley")',	
		'http://www.indeed.com/resumes?q=school%3A("Universal+Life+Church")',	
		'http://www.indeed.com/resumes?q=school%3A("University+of+Devonshire")',	
		'http://www.indeed.com/resumes?q=school%3A("University+of+Newcastle")',	
		'http://www.indeed.com/resumes?q=school%3A("Warren+National+University")',	
		'http://www.indeed.com/resumes?q=school%3A("Washington+International+University")',	
		'http://www.indeed.com/resumes?q=school%3A("Wesleyan+International+University")',	
		'http://www.indeed.com/resumes?q=school%3A("Wilson+State+University")',	
		'http://www.indeed.com/resumes?q=school%3A("Youngsfield+University")',	
		]
	'''	
		
	'''
	Dubious Credit
	
	start_urls = [
		'http://www.indeed.com/resumes?q=school%3A("Almeda+International+University")',
		'http://www.indeed.com/resumes?q=school%3A("Almeda+International+University")',
		'http://www.indeed.com/resumes?q=school%3A("American+Global+International+University")',
		'http://www.indeed.com/resumes?q=school%3A("Cambell+State+University")',
		'http://www.indeed.com/resumes?q=school%3A("Central+State+University+of+New+York")',
		'http://www.indeed.com/resumes?q=school%3A("Colton+State+University")',
		'http://www.indeed.com/resumes?q=school%3A("Columbus+University")',
		'http://www.indeed.com/resumes?q=school%3A("Divine+Heart+College")',
		'http://www.indeed.com/resumes?q=school%3A("Glendale+University")',
		'http://www.indeed.com/resumes?q=school%3A("Hamilton+University")',
		'http://www.indeed.com/resumes?q=school%3A("Hill+University")',
		'http://www.indeed.com/resumes?q=school%3A("Kingston+University")',
		'http://www.indeed.com/resumes?q=school%3A("Lorenz+University")',
		'http://www.indeed.com/resumes?q=school%3A("Midtown+University")',
		'http://www.indeed.com/resumes?q=school%3A("Montgomery+University")',
		'http://www.indeed.com/resumes?q=school%3A("Northern+Point+University")',
		'http://www.indeed.com/resumes?q=school%3A("Olford+Walters+University")',
		'http://www.indeed.com/resumes?q=school%3A("Panworld+University")',
		'http://www.indeed.com/resumes?q=school%3A("Princely+International+University")',
		'http://www.indeed.com/resumes?q=school%3A("Rise+University")',
		'http://www.indeed.com/resumes?q=school%3A("Saint+James+College")',
		'http://www.indeed.com/resumes?q=school%3A("San+Francisco+Institute+of+Architecture")',
		'http://www.indeed.com/resumes?q=school%3A("San+Francisco+Technical+University")',
		'http://www.indeed.com/resumes?q=school%3A("Trinity+College+Theological+Seminary")',
		'http://www.indeed.com/resumes?q=school%3A("Rise+University")',
		'http://www.indeed.com/resumes?q=school%3A("University+of+St+Linus+California")',
		'http://www.indeed.com/resumes?q=school%3A("Western+Advance+Central+University")',
		'http://www.indeed.com/resumes?q=school%3A("Western+Valley+Central+University")'
	]
	'''
	
	'''
	nationally accredited
	
	start_urls = [
		'http://www.indeed.com/resumes?q=school%3A("American+Sentinel+University")',
		'http://www.indeed.com/resumes?q=school%3A("Anaheim+University")',
		'http://www.indeed.com/resumes?q=school%3A("Andrew+Jackson+University")',
		'http://www.indeed.com/resumes?q=school%3A("California+Coast+University")',
		'http://www.indeed.com/resumes?q=school%3A("California+Intercontinental+University")',
		'http://www.indeed.com/resumes?q=school%3A("Cardean+University")',
		'http://www.indeed.com/resumes?q=school%3A("Cleveland+Institite+of+Electronics")',
		'http://www.indeed.com/resumes?q=school%3A("Columbia+Southern+University")',
		'http://www.indeed.com/resumes?q=school%3A("Everest+University")',
		'http://www.indeed.com/resumes?q=school%3A("Florida+Metropolitan+University")',
		'http://www.indeed.com/resumes?q=school%3A("Grantham+University")',
		'http://www.indeed.com/resumes?q=school%3A("Harrison+University")',
		'http://www.indeed.com/resumes?q=school%3A("ITT+Technical+Institute")',
		'http://www.indeed.com/resumes?q=school%3A("Penn+Foster+Career+College")',
		'http://www.indeed.com/resumes?q=school%3A("Professional+Career+Development+Institute")',
		'http://www.indeed.com/resumes?q=school%3A("Southwest+University")',
		'http://www.indeed.com/resumes?q=school%3A("Virginia+College")',
		'http://www.indeed.com/resumes?q=school%3A("Westwood+College")',
		'http://www.indeed.com/resumes?q=school%3A("Windsor+College")',
	]
	
	'''
	
	'''
	Community College
	'''
	
	start_urls = [
		'http://www.indeed.com/resumes?q=school%3A("Alabama+Southern+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Calhoun+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Gadsden+State+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("South+Arkansas+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Pikes+Peak+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Asnuntuck+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Capital+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Manchester+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Norwalk+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Quinebaug+Valley+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Gwinnett+Technical+College")',
		'http://www.indeed.com/resumes?q=school%3A("Heald+College")',
		'http://www.indeed.com/resumes?q=school%3A("Windward+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Black+Hawk+College")',
		'http://www.indeed.com/resumes?q=school%3A("Lincoln+Trail+College")',
		'http://www.indeed.com/resumes?q=school%3A("Wabash+Valley+College")',
		'http://www.indeed.com/resumes?q=school%3A("Parkland+College")',
		'http://www.indeed.com/resumes?q=school%3A("Waubonsee+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Bowling+Green+Technical+College")',
		'http://www.indeed.com/resumes?q=school%3A("Hopkinsville+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Kennebec+Valley+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Leech+Lake+Tribal+College")',
		'http://www.indeed.com/resumes?q=school%3A("Century+College")',
		'http://www.indeed.com/resumes?q=school%3A("Hibbing+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Metropolitan+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Nebraska+College+of+Technical+Agriculture")',
		'http://www.indeed.com/resumes?q=school%3A("Burlington+County+College")',
		'http://www.indeed.com/resumes?q=school%3A("County+College+of+Morris")',
		'http://www.indeed.com/resumes?q=school%3A("Mercer+County+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("WMohawk+Valley+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Monroe+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Ulster+County+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Dakota+College+at+Bottineau")',
		'http://www.indeed.com/resumes?q=school%3A("Hocking+College")',
		'http://www.indeed.com/resumes?q=school%3A("Lorain+County+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Manor+College")',
		'http://www.indeed.com/resumes?q=school%3A("Pennsylvania+Institute+of+Technology")',
		'http://www.indeed.com/resumes?q=school%3A("Westmoreland+County+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Sisseton+Wahpeton+College")',
		'http://www.indeed.com/resumes?q=school%3A("Motlow+State+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Northeast+State+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Walters+State+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Snow+College")',
		'http://www.indeed.com/resumes?q=school%3A("Sargeant+Reynolds+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Patrick+Henry+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Virginia+Highlands+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Institute+for+Extended+Learning")',
		'http://www.indeed.com/resumes?q=school%3A("Spokane+Falls+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Tacoma+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Casper+College")',
		'http://www.indeed.com/resumes?q=school%3A("Sheridan+College")',
		'http://www.indeed.com/resumes?q=school%3A("Guam+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Kenai+Peninsula+College")',
		'http://www.indeed.com/resumes?q=school%3A("Allan+Hancock+College")',
		'http://www.indeed.com/resumes?q=school%3A("Golden+West+College")',
		'http://www.indeed.com/resumes?q=school%3A("Orange+Coast+College")',
		'http://www.indeed.com/resumes?q=school%3A("College+of+Marin")',
		'http://www.indeed.com/resumes?q=school%3A("College+of+the+Redwoods")',
		'http://www.indeed.com/resumes?q=school%3A("Cuesta+College")',
		'http://www.indeed.com/resumes?q=school%3A("Mount+San+Antonio+College")',
		'http://www.indeed.com/resumes?q=school%3A("Napa+Valley+College")',
		'http://www.indeed.com/resumes?q=school%3A("Cypress+College")',
		'http://www.indeed.com/resumes?q=school%3A("College+of+Alameda")',
		'http://www.indeed.com/resumes?q=school%3A("Santiago+Canyon+College")',
		'http://www.indeed.com/resumes?q=school%3A("Moreno+Valley+College")',
		'http://www.indeed.com/resumes?q=school%3A("San+Joaquin+Valley+College")',
		'http://www.indeed.com/resumes?q=school%3A("Evergreen+Valley+College")',
		'http://www.indeed.com/resumes?q=school%3A("Irvine+Valley+College")',
		'http://www.indeed.com/resumes?q=school%3A("Clear+Lake+College")',
		'http://www.indeed.com/resumes?q=school%3A("Yuba+College")',
		'http://www.indeed.com/resumes?q=school%3A("Ancilla+College")',
		'http://www.indeed.com/resumes?q=school%3A("Iowa+Western+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Brown+Mackie+College")',
		'http://www.indeed.com/resumes?q=school%3A("Butler+County+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Flint+Hills+Technical+College")',
		'http://www.indeed.com/resumes?q=school%3A("Northwest+Kansas+Technical+College")',
		'http://www.indeed.com/resumes?q=school%3A("Baton+Rouge+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Frederick+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Bay+de+Noc+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Mississippi+Delta+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Mississippi+Gulf+Coast+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Mineral+Area+College")',
		'http://www.indeed.com/resumes?q=school%3A("North+Central+Missouri+College")',
		'http://www.indeed.com/resumes?q=school%3A("Deep+Springs+College")',
		'http://www.indeed.com/resumes?q=school%3A("Luna+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Cape+Fear+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Martin+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Randolph+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Richmond+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Wayne+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Carl+Albert+State+College")',
		'http://www.indeed.com/resumes?q=school%3A("Western+Oklahoma+State+College")',
		'http://www.indeed.com/resumes?q=school%3A("Treasure+Valley+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Angelina+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Mountain+View+College")',
		'http://www.indeed.com/resumes?q=school%3A("Northeast+Texas+Community+College")',
		'http://www.indeed.com/resumes?q=school%3A("Temple+College")',
		'http://www.indeed.com/resumes?q=school%3A("Gateway+Technical+College")',
		'http://www.indeed.com/resumes?q=school%3A("Waukesha+County+Technical+College")',
	]
	
	
	'''
	#regionally accredited
	start_urls = [
		'http://www.indeed.com/resumes?q=school%3A("Windsor+College")',
		'http://www.indeed.com/resumes?q=school%3A("American+Intercontinental+University")',
		'http://www.indeed.com/resumes?q=school%3A("American+Military+University")',
		'http://www.indeed.com/resumes?q=school%3A("Ashford+University")',
		'http://www.indeed.com/resumes?q=school%3A("Baker+College")',
		'http://www.indeed.com/resumes?q=school%3A("Bellevue+University")',
		'http://www.indeed.com/resumes?q=school%3A("Capella+University")',
		'http://www.indeed.com/resumes?q=school%3A("Charter+Oak+State+College")',
		'http://www.indeed.com/resumes?q=school%3A("Devry+University")',
		'http://www.indeed.com/resumes?q=school%3A("Excelsior+College")',
		'http://www.indeed.com/resumes?q=school%3A("Jones+International+University")',	
		'http://www.indeed.com/resumes?q=school%3A("Excelsior+College")',
		'http://www.indeed.com/resumes?q=school%3A("Kaplan+College")',
		'http://www.indeed.com/resumes?q=school%3A("Keiser+College")',
		'http://www.indeed.com/resumes?q=school%3A("New+York+Institute+of+Technolog")',		
		'http://www.indeed.com/resumes?q=school%3A("Northcentral+University")',
		'http://www.indeed.com/resumes?q=school%3A("Norwich+University")',
		'http://www.indeed.com/resumes?q=school%3A("Regis+University")',
		'http://www.indeed.com/resumes?q=school%3A("Saint+Leo+University")',
		'http://www.indeed.com/resumes?q=school%3A("South+University")',
		'http://www.indeed.com/resumes?q=school%3A("Strayer+University")',
		'http://www.indeed.com/resumes?q=school%3A("Suffolk+University")',
		'http://www.indeed.com/resumes?q=school%3A("Thomas+Edison+State+College")',
		'http://www.indeed.com/resumes?q=school%3A("Touro+University+International")',
		'http://www.indeed.com/resumes?q=school%3A("University+of+Phoenix")',
		'http://www.indeed.com/resumes?q=school%3A("Walden+University")',
		'http://www.indeed.com/resumes?q=school%3A("Webster+University")',		
		'http://www.indeed.com/resumes?q=school%3A("Western+Governors+University")',	
		'http://www.indeed.com/resumes?q=school%3A("Western+International+University")',	
	]
	'''
	

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
		

