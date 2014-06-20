from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import FormRequest
from steampowered.items import SteampoweredItem

class SteampoweredComSpider(CrawlSpider):
    name = 'steampowered_com'
    allowed_domains = ['store.steampowered.com']

    rules = (
        Rule(SgmlLinkExtractor(allow=r'genre/'), follow=True),
        Rule(SgmlLinkExtractor(allow=r'app/\d+'), callback='parse_item')
    )

    def start_requests(self):
        request = FormRequest('http://store.steampowered.com/agecheck/app/252490/', 
            formdata={'ageDay': '1', 'ageMonth': 'January', 'ageYear': '1980'}, 
            callback=self.parse)

        return [request]

    def parse_item(self, response):
        sel = Selector(response)
        i = SteampoweredItem()

        i['name']           = ''.join(sel.xpath('normalize-space(//*[@id="main_content"]//*[@class="block_content_inner"]//*[contains(text(), "Title")]/following-sibling::text())').extract())
        videosvars          = sel.xpath('normalize-space(//*[@id="highlight_player_area"]/*[1]/script)').re(r'[src|data\-hd\-src|poster]=("http\://.*?")')

        try:
            i['video']      = videosvars[0]
        except IndexError:
            i['video']      = ''

        try:
            i['video_hd']   = videosvars[1]
        except IndexError:
            i['video_hd']   = ''

        try:
            i['poster']   = videosvars[2]
        except IndexError:
            i['poster']   = ''

        i['genres']         = sel.xpath('//*[@id="main_content"]//*[@class="block_content_inner"]//*[contains(text(), "Developer")]/preceding-sibling::a//text()').extract()
        if not i['genres']:
            i['genres']     = sel.xpath('//*[@id="main_content"]//*[@class="block_content_inner"]//*[contains(text(), "Publisher")]/preceding-sibling::a//text()').extract()

        i['developer']      = ''.join(sel.xpath('normalize-space(//*[@id="main_content"]//*[@class="block_content_inner"]//*[contains(text(), "Developer")]/following-sibling::a[1]/text())').extract())
        i['publisher']      = ''.join(sel.xpath('normalize-space(//*[@id="main_content"]//*[@class="block_content_inner"]//*[contains(text(), "Publisher")]/following-sibling::a[1]/text())').extract())
        i['release_date']   = ''.join(sel.xpath('normalize-space(//*[@id="main_content"]//*[@class="block_content_inner"]//*[contains(text(), "Release Date")]/following-sibling::text())').extract())
        i['languages']      = sel.xpath('//*[@id="main_content"]//*[@class="game_language_options"]//tr[position() > 1]/th[1]//text()').extract()
        i['about']          = ''.join(sel.xpath('normalize-space(//*[@id="game_highlights"]//*[@class="game_description_snippet"]/text())').extract())
        i['website']        = ''.join(sel.xpath('normalize-space(//*[@id="main_content"]//*[@class="block_content_inner"]//a[@class="linkbar" and contains(., "website")]/@href)').extract())
        
        macSel  = sel.xpath('//*[@id="game_area_sys_req"]/h2[contains(., "Mac System")]/..')
        pcSel   = sel.xpath('//*[@id="game_area_sys_req"]/h2[contains(., "PC System")]/..')

        if not macSel and not pcSel:
            pcSel   = sel.xpath('//*[@id="game_area_sys_req"]/h2[contains(., "System")]/..')

        i['requirements'] = {
            'mac': {
                "minimum": {
                    'os':           ''.join(macSel.xpath('normalize-space(//*[contains(@id, "left")]//*[contains(text(), "OS")]/following-sibling::text())').extract()),
                    'processor':    ''.join(macSel.xpath('normalize-space(//*[contains(@id, "left")]//*[contains(text(), "Processor")]/following-sibling::text())').extract()),
                    'memory':       ''.join(macSel.xpath('normalize-space(//*[contains(@id, "left")]//*[contains(text(), "Memory")]/following-sibling::text())').extract()),
                },
                "recommended": {
                    'os':           ''.join(macSel.xpath('normalize-space(//*[contains(@id, "right")]//*[contains(text(), "OS")]/following-sibling::text())').extract()),
                    'processor':    ''.join(macSel.xpath('normalize-space(//*[contains(@id, "right")]//*[contains(text(), "Processor")]/following-sibling::text())').extract()),
                    'memory':       ''.join(macSel.xpath('normalize-space(//*[contains(@id, "right")]//*[contains(text(), "Memory")]/following-sibling::text())').extract()),
                },
            },
            'pc': {
                "minimum": {
                    'os':           ''.join(pcSel.xpath('normalize-space(//*[contains(@id, "left")]//*[contains(text(), "OS")]/following-sibling::text())').extract()),
                    'processor':    ''.join(pcSel.xpath('normalize-space(//*[contains(@id, "left")]//*[contains(text(), "Processor")]/following-sibling::text())').extract()),
                    'memory':       ''.join(pcSel.xpath('normalize-space(//*[contains(@id, "left")]//*[contains(text(), "Memory")]/following-sibling::text())').extract()),
                    'directx':      ''.join(pcSel.xpath('normalize-space(//*[contains(@id, "left")]//*[contains(text(), "DirectX")]/following-sibling::text())').extract()),
                    'hard_drive':   ''.join(pcSel.xpath('normalize-space(//*[contains(@id, "left")]//*[contains(text(), "Hard Drive")]/following-sibling::text())').extract()),
                    'network':      ''.join(pcSel.xpath('normalize-space(//*[contains(@id, "left")]//*[contains(text(), "Network")]/following-sibling::text())').extract()),
                },
                'recommended': {
                    'os':           ''.join(pcSel.xpath('normalize-space(//*[contains(@id, "right")]//*[contains(text(), "OS")]/following-sibling::text())').extract()),
                    'processor':    ''.join(pcSel.xpath('normalize-space(//*[contains(@id, "right")]//*[contains(text(), "Processor")]/following-sibling::text())').extract()),
                    'memory':       ''.join(pcSel.xpath('normalize-space(//*[contains(@id, "right")]//*[contains(text(), "Memory")]/following-sibling::text())').extract()),
                    'directx':      ''.join(pcSel.xpath('normalize-space(//*[contains(@id, "right")]//*[contains(text(), "DirectX")]/following-sibling::text())').extract()),
                    'hard_drive':   ''.join(pcSel.xpath('normalize-space(//*[contains(@id, "right")]//*[contains(text(), "Hard Drive")]/following-sibling::text())').extract()),
                    'network':      ''.join(pcSel.xpath('normalize-space(//*[contains(@id, "right")]//*[contains(text(), "Network")]/following-sibling::text())').extract()),
                },
            }
        }

        return i
