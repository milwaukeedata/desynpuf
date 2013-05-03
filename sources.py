#!/usr/bin/env python
import simplejson as json
import os
from sh import wget, cd, unzip, rm

C = json.load(open('sources.json'))
mydir = os.path.dirname(os.path.realpath(__file__)) + '/sources/'

for k in C.keys():
  if not os.path.exists(mydir + k):
    print "mkdir %s%s" % (mydir, k)
    os.makedirs(mydir + k)
    for source in C[k]:
      file_name = mydir + k + source.split('/')[-1]
      print "wget -nc -O %s %s" % (file_name, source)
      wget('-nc', '-O', file_name, source)
      print "unzip -d %s %s" % (mydir + k, file_name)
      unzip('-d', mydir + k, file_name)
      print "rm %s" % file_name
      rm(file_name)
