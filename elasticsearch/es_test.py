'''
Created on Jun 25, 2014

@author: jimhorng
'''
from elasticsearch import Elasticsearch
es = Elasticsearch(hosts=[{'host': '192.168.69.41', 'port': 9200}])

# body = {
#     '@timestamp': "2014-06-20T09:30:12.000Z",
#     '@version' : "1",
#     'id': "xxx",
#     'type': "gitlab",
#     'repository': {
#         'name': "tunnel",
#         'url': "git@gitlab.myqnapcloud.com:qcloud/tunnel.git",
#         'description': "",
#         'homepage': "http://gitlab.myqnapcloud.com/qcloud/tunnel"
#     },
#     'commit': {
#         'id': "8800631570d1929d7f05f9d24ceaaf9fe3d1a1e9",
#         'message': "Pre-generate chunk sample for mock testing.",
#         'url': "http://gitlab.myqnapcloud.com/qcloud/tunnel/commit/8800631570d1929d7f05f9d24ceaaf9fe3d1a1e8",
#         'author': {
#             'name': "test",
#             'email': "test@qnap.com",
#         }
#     }
# }
# 
# res = es.create(index="gitlab", doc_type='gitlab', body=body, id="8800631570d1929d7f05f9d24ceaaf9fe3d1a1e9")
# 
# print(res)

res = es.delete(index="gitlab", doc_type='gitlab', id='Ik2iDMAPRki9L7MIal59Jw')
print res