# 大致代码如下：
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from django.db import connection
from multiprocessing import Process
from eco_spider.spiders.seo_spider import StackoverflowSpider
from celery import shared_task
from celery.signals import worker_process_init



class Urls(object):
    url = ''
    base_url = ''


class BilliardCrawlProcess(Process):

    def run(self):
        settings = get_project_settings()
        process = CrawlerProcess(settings)
        process.crawl('stackoverflow', )
        process.start()


def transfer_url(url, short_url):
    urls = Urls
    urls.url = url
    urls.base_url = short_url

    # NOTE


@shared_task
def crawl(url, short_url):
    urls = StackoverflowSpider()
    urls.get_url(url, short_url)
    crawl_process = BilliardCrawlProcess()

    crawl_process.start()
    crawl_process.join()  # blocks here until scrapy finished
    connection.close()

@worker_process_init.connect
def fix_multiprocessing(**kwargs):
    from multiprocessing import current_process
    try:
        current_process()._config
    except AttributeError:
        current_process()._config = {'semprefix': '/mp'}
