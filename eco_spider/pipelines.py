# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from ecoapp.models import (Questions, Results)
from eco_spider.check_seo import Check
import datetime
from ecoapp.models import Results, Prov


class QuestionItemPipeline(object):
    def process_item(self, item, spider):
        # date_add = datetime.date.today()
        #
        # title = item['title']
        #
        # if item['keyword'] is not None:
        #     keywords = item['keyword']
        #
        # else:
        #     keywords = 'Ошибок нет'
        #
        # if item['description'] is not None:
        #     descriptions = item['description']
        #
        # else:
        #     descriptions = 'Ошибок нет'
        #
        # if item['h1'] is not None:
        #     h1 = item['h1']
        #
        # else:
        #     h1 = 'Ошибок нет'
        #
        # if item['googl_anal'] is not None:
        #     google = item['googl_anal']
        #
        # else:
        #     google = 'Ошибок нет'
        #
        # if item['h2'] is not None:
        #     h2 = item['h2']
        #
        # else:
        #     h2 = 'Ошибок нет'
        #
        # if item['yandex_metrick'] is not None:
        #     yandex = item['yandex_metrick']
        #
        # else:
        #     yandex = 'Ошибок нет'
        #
        # vk = item['vk']
        # facebook = item['facebook']
        # instagram = item['instagram']
        # broken_link = item['broken_link']
        # base_url = item['base_url']
        # title_unique = item['title_unique']
        # desc_unique = item['description_unique']
        # results = Prov(title=item['link'])
        # results = Results(base_url=base_url, title=title, url=item['link'], keywords=keywords,
        #                   description=descriptions, title_unique=title_unique, description_unique=desc_unique,
        #                   h1=h1, h2=h2, vk=vk, facebook=facebook, instagram=instagram, google=google,
        #                   yandex=yandex, broken_link=broken_link, date_add=date_add)
        item.save()
        return item
