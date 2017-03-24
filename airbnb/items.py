# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AirbnbItem(scrapy.Item):
  property_id = scrapy.Field()
  url = scrapy.Field()
  description = scrapy.Field()
  detail = scrapy.Field()
  def __unicode__(self):
    return repr(self).decode('unicode_escape')
  pass
