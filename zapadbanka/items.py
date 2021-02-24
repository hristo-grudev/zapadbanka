import scrapy


class ZapadbankaItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
