# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class SteampoweredItem(Item):
    name            = Field()
    poster          = Field()
    video           = Field()
    video_hd        = Field()
    genres          = Field()
    developer       = Field()
    publisher       = Field()
    release_date    = Field()
    languages       = Field()
    about           = Field()
    website         = Field()
    warning         = Field()
    requirements    = Field()
