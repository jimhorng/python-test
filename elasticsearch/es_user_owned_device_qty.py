'''
Created on Jun 25, 2014

@author: jimhorng
'''
from elasticsearch import Elasticsearch
es = Elasticsearch(hosts=[{'host': '192.168.69.41', 'port': 9200}])

body = {
    "size": 0,
    "aggs" : {
        "test_aggr" : {
            "terms" : {
                "field" : "user_id"
            }
        }
    }
}


res = es.search(index="mongo", doc_type='device', body=body)

user_owned_nas_qty = res['aggregations']['test_aggr']['buckets']

for record in user_owned_nas_qty:
    record['user_id'] = record.pop('key')
    record['owned_nas_qty'] = record.pop('doc_count')
    es.create(index="result_temp", doc_type="user_owned_nas_qty", body=record)

print(user_owned_nas_qty)