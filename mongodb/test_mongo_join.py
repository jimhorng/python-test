import pymongo

from pymongo import MongoClient
from bson.json_util import dumps

client = MongoClient('192.168.68.234', 27017)

db = client.qcloud

licenses_record = db.license.find(
    { 'user_id': "531440cecc095d1a8cd83c5a" }
)

licenses = dict(licenses_record)

device_ids = [ the_license['applied_on_device_id'] for the_license in licenses if the_license.get('applied_on_device_id') ]

print "licenses: " + dumps(licenses)
print "device_ids: " + str(device_ids)

devices = db.device.find(
    { '_id': { '$in': device_ids } }
)

devices_dict = { 'device_id' : device['_id'] for device in devices }

for the_license in licenses:
    if the_license.get('applied_on_device_id'):
        the_license['device_model_name'] = devices_dict.get(the_license.get('applied_on_device_id'))

print dumps(licenses)

# pairs = pair_collection.find({'receiver_reg_id': "76d1f75c4249efe0cf14af70acef799fd783e561c88e3ca6839f07c913ef646f"})
# 
# for pair in pairs:
#     print pair