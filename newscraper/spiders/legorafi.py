import scrapy
import json
import os

class LeGorafi(scrapy.Spider):
    name = "legorafi"

    start_urls = [
        f'https://www.legorafi.fr/category/france/politique/page/{x}' 
        for x in range(1, 50)
    ]

    def parse(self, response):
        urls = response.css('.mvp-blog-story-list  a::attr(href)').getall()
        urls += response.css('#mvp-cat-feat-wrap  a::attr(href)').getall()
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_article)

    def parse_article(self, response):
        data = {
            'title': response.css('.mvp-post-title::text').get(),
            'author': response.css('.author-name a::text').get(),
            'description': ' '.join(response.css('.mvp-post-excerpt *::text').getall()),
            'date': response.css('time.post-date::attr(datetime)').get(),
            'content':' '.join(response.css('#mvp-content-main > p *::text').getall())
        }
        with open(os.path.join('legorafi_data/', response.url.split('/')[-2]) + '.json', 'w', encoding='utf-8') as f:
           json.dump(data, f, ensure_ascii=False)


