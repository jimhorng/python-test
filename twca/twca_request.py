# -*- coding: utf-8 -*-
'''
Created on Nov 26, 2014

@author: jimhorng
'''

import M2Crypto
import os
import xml.etree.ElementTree as ET

TESTDATA_PATH = "/Users/jimhorng/workspace/twca/testdata"
CSR_PATH = os.path.join(TESTDATA_PATH, 'test2.csr.pem')
CSR_B64 = "MIICnDCCAYQCAQAwVzELMAkGA1UEBhMCVFcxDDAKBgNVBAgTA1RQRTENMAsGA1UEBxMEdGVzdDENMAsGA1UEChMEdGVzdDENMAsGA1UECxMEdGVzdDENMAsGA1UEAxMEdGVzdDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMSLA4wpIq8ySJr8OW0JSGe0NPsFCe4vtcS6joz3Tm1Ffga/ieOSbV3fqAdO+AulmCwU4+Ggo7QuOgVuM6OmJ3WsFU7yaShcHNi8sYjMQQNGIMHr3vpz2N21r+xxbEOl0Hs/9vKzKwfiX1j+BRySiks3a3k5JVhxCkd0awfQ09BnoW75dTyizkFJmcNoI/tAc9I50pEFuD90t/QU6b6rVDZSieqDpQTByx+n6mxUPiO1i2+cMOLpBFvNpaBZNeALTz3U6QujGCfsuTfVDa8yzLks0UxmBANhov5Id016DKx4nivpzPDpbi0fMQ8ivKEjl5GYggA4jMZ3r7vXA/US31sCAwEAAaAAMA0GCSqGSIb3DQEBCwUAA4IBAQBA31E5Zw2pDeEOMN+hjqHWYfCzVOi843jje9b9Tmhkn+6wJ4T9jqsPK/O0blWEsnc3pEq2wHY6R+YPwIcNdy+cXmuNTqSQ0V/5CCx3/fKbPGfSWe+WC0XYZFVK7sLti/8lNZlSPS19DgPyczZZRYUiaLit4y3+c50uVhbey/j0tRKqnE79+Mvs86GLXoMI2CFQWcJ1L0rXavwrkKd+zAw6J+hoFL5egPsp6JZ5OmrRGeEGmOS0+gH5tVRTqzeVVl1oZT1YmURXLAL0Ap52u+LKbucy13ojPEv1GxzMxWpoOM+RcrWHPcPUqFZF4YIpbYUS2B6vB0YkzlDoJM8GYCOY"

def build_xml():
    test_tag = ET.Element('request')
    version_tag = ET.SubElement(parent=test_tag, tag='version')
    version_tag.text = "1"
    applyid_tag = ET.SubElement(parent=test_tag, tag='applyid')
    applyid_tag.text = "0000001"
    csr_tag = ET.SubElement(parent=test_tag, tag='csr')
    csr_tag.text = CSR_B64
    notafter_tag = ET.SubElement(parent=test_tag, tag='notafter')
    notafter_tag.text = "2013-11-25T23:59:59+08:00"
    type_tag = ET.SubElement(parent=test_tag, tag='type')
    type_tag.text = "1"
#     serial_tag = ET.SubElement(parent=test_tag, tag='serial')
#     serial_tag.text = "1"
    print ET.tostring(test_tag, encoding="UTF-8")
    ET.ElementTree(test_tag).write('testunicode.xml',encoding="UTF-8",xml_declaration=True)

def main():
    build_xml()

if __name__ == '__main__':
    main()