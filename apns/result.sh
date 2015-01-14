#/bin/bash
echo "*** amount of conn reset:"
cat log | grep "exception occur when reading APNS error-response"
echo "*** total err response get:"
cat log | grep "got error-response from APNS" | wc -l
