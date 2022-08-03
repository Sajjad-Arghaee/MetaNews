import scrapy
from ..items import MetanewscrawlerItem
from scrapy.http import Response, Request
from users.models import Profile


class TechnologySpider(scrapy.Spider):
    name = 'technology_spider'
    start_urls = [
        'https://www.euronews.com/next/next-series/sci-tech'
    ]
    counter = 0

    def parse(self, response: Response, **kwargs):
        links = response.css('.m-modeXL-1 .m-object__title__link::attr(href)').extract()
        temp_dict = {'image': response.css('.m-img.lazyload::attr(data-src)').extract()}
        for link in links:
            yield Request(url='https://www.euronews.com/'+link,
                          callback=self.parse_link,
                          dont_filter=False,
                          cb_kwargs={'temp_dict': temp_dict})

    def parse_link(self, response: Response, temp_dict):
        item = MetanewscrawlerItem()
        title = response.css('.u-text-align--start::text').extract_first().replace('\n', '').replace('\\', '').strip()
        description = ' '.join(response.css('.js-article-content p::text').extract()).replace('\n', '').replace('\\', '').strip()
        item['topic'] = 'technology'
        item['title'] = title
        item['description'] = description
        item['image'] = temp_dict['image'][self.counter]
        self.counter += 1
        item['author'] = Profile.objects.get(name='euronews')
        yield item
