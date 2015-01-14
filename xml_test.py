'''
Created on Dec 4, 2014

@author: jimhorng
'''

import xml.etree.ElementTree as ET

xml_string = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><response><applyid>9059636f-2a8a-40d9-9a07-87bc518b559b</applyid><code>300</code><msg>檢查CSR內容異常, 公鑰重複</msg><time>2014-12-04T11:16:19.986+08:00</time><version>1</version></response>'

root = ET.fromstring(xml_string)