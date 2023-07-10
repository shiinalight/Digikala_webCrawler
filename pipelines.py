# Defining item pipelines 
#
# Adding pipeline to the ITEM_PIPELINES setting

from itemadapter import ItemAdapter


class DigikalaWebCrawlerPipeline:
    def process_item(self, item, spider):
        return item
