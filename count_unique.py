#!/usr/bin/env python
import sys
from glob import glob

def main(data):
  allids = {}
  for line in data:
    synpufid = line.split(',')[0]
    allids[synpufid] = 1
    print '.',
  print len(allids)

if __name__ == '__main__':

  main(sys.stdin.readlines())
