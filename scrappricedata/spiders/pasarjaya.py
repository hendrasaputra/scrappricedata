# -*- coding: utf-8 -*-
import scrapy
from datetime import date

class PasarjayaSpider(scrapy.Spider):
    name = "pasarjaya"
    allowed_domains = ["pasarjaya.co.id"]
    start_urls = (
        'http://www.pasarjaya.co.id/komoditas',
    )
	today = date.today()
    def mapMonth(strMonth):
    	strMonthID = {'Januari':1,'Februari':2,'Maret':3,'April':4,'Mei':5,'Juni':6,'Juli':7,'Agustus':8,'September':9,'Oktober':10,'November':11,'Desember':12}
    	strMonthEN = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}

    	try:
    		return strMonthID[strMonth]
    	except KeyError:
    		return strMonthEN[strMonth]


    def parse(self, response):
        log.msg('parse(%s)' % response.url, level = log.DEBUG)
        tableDetail = response.xpath('//table[@id="detail"]')
        bulanName = tableDetail.xpath('//th[@id="th1" and @colspan="11"]/text()').extract()
        monthNum = mapMonth(bulanName[0].split()[1])

        for row in tableDetail.xpath('//td[@id="td1"]'):
        	for i in len(tableDetail.xpath('(//th[@id="th1" and not(@colspan="11")]/text())'))-1:
        		commodityItem = CommodityItem()
        		commodityItem['datePeriod'] = today.year + monthNum + tableDetail.xpath('(//th[@id="th1" and not(@colspan="11")]/text())[4]')
        	pass