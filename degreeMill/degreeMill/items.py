# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class DegreemillItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass
	
class collegeItem(Item):
	# this item used to store the college
	# here we will keep a list of "graduate"
	graduateList = Field()
	
class resumeItem(Item):
	# this item used to store the resume information
    name = Field()
    jobTime = Field()
    eduTitle = Field()
    eduDates = Field()
    eduSchool = Field()
