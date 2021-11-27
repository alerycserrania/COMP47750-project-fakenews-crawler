import scrapy
import json
import os

class LeMonde(scrapy.Spider):
    name = "lemonde"

    start_urls = [
        'https://www.lemonde.fr/politique/',
        'https://www.lemonde.fr/politique/2',
        'https://www.lemonde.fr/election-presidentielle-2022/',
        'https://www.lemonde.fr/election-presidentielle-2022/2'
    ]

    def parse(self, response):
        urls = response.css('section.page__content a.teaser__link::attr(href)').getall()
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_article)

    def parse_article(self, response):
        data = {
            'title': response.css('.article__title::text').get(),
            'author': response.css('.article__author-link::text').get(),
            'description': ' '.join(response.css('.article__desc *::text').getall()),
            'date': '-'.join(response.url.split('/')[-4:-1]),
            'content':' '.join(response.css('.article__paragraph *::text').getall())
        }
        with open(os.path.join('lemonde_data/', '-'.join(response.url.split('/')[-4:])[:100]) + '.json', 'w', encoding='utf-8') as f:
           json.dump(data, f, ensure_ascii=False)


