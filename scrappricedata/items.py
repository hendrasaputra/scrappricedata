# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrappricedataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    class CommodityItem(scrapy.Item):
    	datePeriod = scrapy.Field()
    	name = scrapy.Field()
    	measure = scrapy.Field()
    	price = scrapy.Field()
    	# group = scrapy.Field()
    	last_updated = scrapy.Field(serializer=str)
