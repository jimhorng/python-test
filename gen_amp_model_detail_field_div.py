'''
Created on Jan 6, 2015

@author: jimhorng
'''

template = """<div class="control-group">
    <label class="control-label">${{_("{label}")}}</label>
    <div class="controls">
        <label class="qcloud-label">{{{{ record.{key} }}}}</label>
    </div>
</div>"""

keys = """
    certificate_transaction_record_id
    status_code
    status_message
    ra_request_time
    ra_request_content
    ra_request_apply_id
    ra_request_type
    ca_response_time
    ca_response_arrival_time
    ca_response_content
    ca_response_code
    ca_response_msg
"""


for key in keys.split():
    label = key.replace('_', " ").title()
    print template.format(label=label, key=key)