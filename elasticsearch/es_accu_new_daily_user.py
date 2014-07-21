'''
Created on Jun 25, 2014

@author: jimhorng
'''
import time
from elasticsearch import Elasticsearch

time_start = time.time()

es = Elasticsearch(hosts=[{'host': '192.168.69.41', 'port': 9200}])

TYPE_NEW_USER_ACCUMULATED = "new_user_accumulated"
INDEX_RESULT_TEMP = "result_temp"
INTERVAL = "day"

#Remove temp result
query_body = {
    "query": {
      "match_all": {}
    }
}

res = es.delete_by_query(index=INDEX_RESULT_TEMP, doc_type=TYPE_NEW_USER_ACCUMULATED, body=query_body)

#Query from raw data
body = {
    "aggs" : {
        "user_over_time" : {
            "date_histogram" : {
                "field" : "created_at",
                "interval" : INTERVAL,
                "min_doc_count" : 0
            }
        }
    }
}


res = es.search(index="mongo", doc_type='user', body=body, size=0)

new_user_weekly_accumulated = res['aggregations']['user_over_time']['buckets']

current_sum = 0
for record in new_user_weekly_accumulated:
    current_sum += record.pop('doc_count')
    record['user_accumulated_count'] = current_sum
    record['created_at'] = record.pop('key_as_string')
    es.create(index=INDEX_RESULT_TEMP, doc_type=TYPE_NEW_USER_ACCUMULATED, body=record)

print(new_user_weekly_accumulated)

print("DEBUG: time elapsed: %s" % (time.time() - time_start))