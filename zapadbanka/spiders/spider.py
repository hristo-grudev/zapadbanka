import scrapy

from scrapy.loader import ItemLoader
from ..items import ZapadbankaItem
from itemloaders.processors import TakeFirst


class ZapadbankaSpider(scrapy.Spider):
	name = 'zapadbanka'
	start_urls = ['https://www.zapadbanka.me/me/naslovna-2/banka-u-javnosti']

	def parse(self, response):
		post_links = response.xpath('//h3[@class="ba-blog-post-title"]/a/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

		next_page = response.xpath('//div[@class="ba-blog-posts-pagination"]//a[@class="ba-btn-transition"]/@href').getall()
		yield from response.follow_all(next_page, self.parse)


	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//div[@class="body"]//div[@class="content-text"]//text()[normalize-space() and not(ancestor::span)]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()

		item = ItemLoader(item=ZapadbankaItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)

		return item.load_item()
