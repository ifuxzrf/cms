from elasticsearch import Elasticsearch
from tools.read_config import SysConfig


class Elasticsearch_crdu(object):
    def __init__(self, host='localhost', port='9200'):
        self.es = Elasticsearch([f'{SysConfig.getValue("elasticsearch", "host")}:'
                                 f'{SysConfig.getValue("elasticsearch", "host")}'])
        self.index_name = 'ibm'
        self.doc_type = 'txts'

    def create_index(self, index_name="ott", index_type="ott_type"):
        """
        创建索引,创建索引名称为ott，类型为ott_type的索引
        :param ex: Elasticsearch对象
        :return:
        """
        # 创建映射
        _index_mappings = {
            "mappings": {
                self.doc_type: {
                    "properties": {
                        "txt_name": {
                            "type": "text",
                            "index": True,
                            "analyzer": "ik_max_word",
                            "search_analyzer": "ik_max_word"
                        },
                        "content": {
                            "type": "text",
                            "index": True,
                            "analyzer": "ik_max_word",
                            "search_analyzer": "ik_max_word"
                        },
                    }
                }
            }
        }

    def create(self, txt_name, content):
        item = {"txt_name": txt_name, "content": content}
        res = self.es.index(index=self.index_name, doc_type=self.doc_type, body=item)
        print(res)

    def bulk_Index_Data(self, item_list):
        pass

    def Delete_Index_data(self, id):
        res = self.es.delete(index=self.index_name, doc_type=self.doc_type, id=id)
        print(res)

    def Get_Data_By_Body(self, keyword, keyvalue):
        doc = {
            "query": {
                "match": {
                    keyword: keyvalue
                }
            }
        }

        _searched = self.es.search(index=self.index_name, doc_type=self.doc_type, body=doc)

        print(_searched)

    def Delete_Multi_Data(self, keyword, keyvalue):
        doc = {
            "query": {
                "match": {
                    keyword: keyvalue
                }
            }
        }
        res = self.es.delete_by_query(index=self.index_name, body=doc, doc_type=self.doc_type)
        print(res)


if __name__ == '__main__':
    es_ope = Elasticsearch_crdu()
    es_ope.create_index()
