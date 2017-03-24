# -*- coding: utf-8 -*-
import scrapy
from airbnb.items import AirbnbItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class AirbnbDetailSpider(scrapy.Spider):
  name = "airbnb_detail"
  allowed_domains = ["www.airbnb.jp"]

  input_file_name = 'url_list.csv'
  input_file_object = open(input_file_name, 'r')
  lines = input_file_object.readlines()

  urls = []

  for line in lines:
    urls.append(line.split(',')[0])

  print(urls)
  start_urls = urls

  def parse(self, response):
    item = AirbnbItem()
    item['detail'] = ",".join(response.xpath("//div[@id='details']/div/div/div/div/div/div/p/span/text()").extract()).strip().replace('\n','')
    item['description'] = " ".join(response.xpath("//div[@id='description']/div/div/div/div/div/div/div/div[@class='simple-format-container']/p/span/text()").extract()).strip().replace('\n','')
    item['detail'] = ",".join(response.xpath("//div[@id='details']/div/div/div/div/div/div/p/span/text()").extract()).strip().replace('\n','')
    item['url'] = response.url
    item['property_id'] = response.url.replace('https://www.airbnb.jp/rooms/','')
    yield item
