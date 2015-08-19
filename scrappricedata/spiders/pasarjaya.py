# -*- coding: utf-8 -*-
import scrapy


class PasarjayaSpider(scrapy.Spider):
    name = "pasarjaya"
    allowed_domains = ["pasarjaya.co.id"]
    start_urls = (
        'http://www.pasarjaya.co.id/',
    )

    def parse(self, response):
        pass
