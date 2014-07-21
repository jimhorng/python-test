'''
Created on Jun 25, 2014

@author: jimhorng
'''
from elasticsearch import Elasticsearch
import dateutil.parser
import time

time_start = time.time()

es = Elasticsearch(hosts=[{'host': '192.168.69.41', 'port': 9200}])


ES_INDEX='gitlab'
ES_TYPE='gitlab'
REPO_NAME="deployer"
commit_log_file = "/Users/jimhorng/workspace/qcloud/" + REPO_NAME + "/commit.log"
REPO_URL="git@gitlab.myqnapcloud.com:qcloud/" + REPO_NAME + ".git"
REPO_HOME_URL="http://gitlab.myqnapcloud.com/qcloud/" + REPO_NAME
COMMIT_URL_PREFIX=REPO_HOME_URL+"/commit/"

body_template = {
    '@timestamp': "2014-06-20T09:30:12.000Z",
    '@version' : "1",
    'id': "xxx",
    'type': "gitlab",
    'repository': {
        'name': "api",
        'url': "git@gitlab.myqnapcloud.com:qcloud/api.git",
        'description': "",
        'homepage': "http://gitlab.myqnapcloud.com/qcloud/tunnel"
    },
    'commit': {
        'id': "8800631570d1929d7f05f9d24ceaaf9fe3d1a1e9",
        'message': "Pre-generate chunk sample for mock testing.",
        'url': "http://gitlab.myqnapcloud.com/qcloud/tunnel/commit/8800631570d1929d7f05f9d24ceaaf9fe3d1a1e8",
        'author': {
            'name': "test",
            'email': "test@qnap.com",
        }
    }
}

index=0
f = open(commit_log_file, "r")
for line in f:
    tokens = line.split("\t")
    commit_sha=tokens[0]
    author_name=tokens[1]
    author_email=tokens[2]
    commit_date=(dateutil.parser.parse(tokens[3])
                    .astimezone(dateutil.tz.tzutc())
                    .strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z")
    message=tokens[4]
    
    body=body_template.copy()
    body['@timestamp']=commit_date
    body['id']=commit_sha
    body['commit']['id']=commit_sha
    body['commit']['url']=COMMIT_URL_PREFIX+commit_sha
    body['commit']['message']=message
    body['commit']['author']['name']=author_name
    body['commit']['author']['email']=author_email
    
    body['type']=ES_TYPE
    body['repository']['name']=REPO_NAME
    body['repository']['url']=REPO_URL
    body['repository']['homepage']=REPO_HOME_URL
    try:
        res = es.create(index=ES_INDEX, doc_type=ES_TYPE, body=body, id=commit_sha)
    except Exception as e:
        print e
    index += 1
    print("DEBUG: index: " + str(index))
 
print("DEBUG: time elapsed: %s" % (time.time() - time_start))