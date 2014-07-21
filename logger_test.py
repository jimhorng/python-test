'''
Created on Jan 29, 2014

@author: jimhorng
'''
import logging

_logger = logging.getLogger(__name__)
_logger.addHandler(logging.StreamHandler())
_logger.setLevel(logging.DEBUG)
# _logger.setLevel(logging.INFO)

debug_msg = "debug test"
info_msg = "info test"
if _logger.isEnabledFor(logging.DEBUG):
    info_msg = info_msg + debug_msg

_logger.info(info_msg)
_logger.error("error test")
_logger.warn("warn test")
