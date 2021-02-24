BOT_NAME = 'zapadbanka'

SPIDER_MODULES = ['zapadbanka.spiders']
NEWSPIDER_MODULE = 'zapadbanka.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'zapadbanka.pipelines.ZapadbankaPipeline': 100,

}

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
