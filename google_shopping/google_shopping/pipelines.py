# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter



class GoogleShoppingPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        #field name: price
        field_name = 'price'
        value = adapter.get(field_name)
        value = value[2:]
        adapter[field_name] = float(value)

        #field name: link
        field_name = 'link'
        value = adapter.get(field_name)
        value = value[9:]
        adapter[field_name] = value


        return item
