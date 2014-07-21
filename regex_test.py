'''
Created on Feb 20, 2014

@author: jimhorng
'''

import re

pattern_logged = r"\[(\d+-\d+-\d+ \d+:\d+:\d+,\d+): WARNING/Worker-\d+\] msg got.+"
s = "[2014-02-20 10:51:21,753: WARNING/Worker-1] msg got:...TLBLYYVLZGWDWAAWEHCJGEHXWCUKMOATGRVNGIMZGULSJATOUDJZCWIBRAAGXEMIYCEBYOYNHUQGWEIFQHOZYLSMKJSTKSWYCUAFYWHNSPJRVYBZQYFXOZDSDZZIYPIOKIORLXZQQPKNFPIBLQZWTKMMWBKDVAEYPILESNWSSSPWNBCJJKTIAVMAUSKABBZIWPZSEYKVNGGAUHACTNPDHYTZWPKNIIAXPSDMFFGAEYDKTOQGHTJICRGHALSBYKVQ"

test = []

pa1 = r"^qnap.*$|^apns$"
s0 = "apns"
s1 = "apnsx"
s2 = "xapns"
s3 = "xapnsx"
s4 = "xqnap.comx"
s5 = "qnap.com"
s6 = "qnapcom"

print re.match(pa1, s0)
print re.match(pa1, s1)
print re.match(pa1, s2)
print re.match(pa1, s3)
print re.match(pa1, s4)
print re.match(pa1, s5)
print re.match(pa1, s6)

if __name__ == '__main__':
    pass