from gcm import GCM
import time
import datetime
import json

API_KEY = "AIzaSyCDi8l6NJXDVimtAUml21PrYX8t5_vJadA"

gcm = GCM(API_KEY)

timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

msg_body = 'test from python gcm sender...' + timestamp
data = {'price': msg_body, 
        'message': msg_body}

reg_id_1 = "APA91bGMs0qLJl_b0PKDvrPM01rFeD2a3OOx5Vyux2O307RXwuxPOTe3UqimW6X4tWCTaMQmpRJMz8_AL_1ZXc5VJueknagM0RFs92KiRgfaIJtlzCfSx3NureUdz8dV5EQzBZgw50xJVFltne1hv9GaaJZExrdzDQ4VjMzbQxlftuPgrnRwroI"
reg_id_jeff = 'APA91bH09zcPGWKFXkZ1rfP-2VO_rq-hbQjHI9iJky-wcRL1YBWxM3Y2OZYXXzYBprPKTUOUkeAnOb7kK_6CSWLQsrWgCNOMXnH3ImZ_lj4Yb32icf4zFcAlAQRYP0U-hL3uM-njbyTcNFuHhtGv693H_Ok6k95BvQ'

reg_ids = [reg_id_jeff]

# reg_ids = ['APA91bG6u48DriQFYqzt6bd_q7ndxLM3HVaIum8-LO-PMWbU8cksPgsFW1VeAUbC23aqQ20VAHoGagHkIW2yGTtk1OW8k1zt6sNCAU_vT5S24tvgD0qyho4INIrheDtAeh1qabMWd5ACUhv5rfsFkcxeLgDmJu_LhLX6uPS0xU0mApmGYTQWs3I',
#            'APA91bEwb1qt2BOe50w-SiyYdtdaum5LnN166KSnO2h0Jv_XP8s0Bxkvgt9sIYL3VB52zDfG_YPOuBmL1zuXX8Gui68zD2sLyMSD67EPIMyh5NSa5FpT67HB4bhd7T7q6bKntNIJ4cKHTAotSzCezynn1qku5belN2F1BhnTa2JhmbOLu7m0KD4']
response = gcm.json_request(registration_ids=reg_ids, data=data)

print "sent: " + msg_body
print json.dumps(response)