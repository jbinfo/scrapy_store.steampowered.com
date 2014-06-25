# Scrapy settings for steampowered project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'steampowered'

SPIDER_MODULES = ['steampowered.spiders']
NEWSPIDER_MODULE = 'steampowered.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = '"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"'
