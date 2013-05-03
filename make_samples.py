#!/usr/bin/env python

"""
Given a handful of CSVs, the first column of each is a unique identifier,
create sample sets limited to the same identifiers.
"""

import os
import sys
from glob import glob
import random
import unittest
from expecter import expect

class Synpuf(object):
  def __init__(self, sample_number, sample_size, filenames, new_directory):
    self.sample_number = sample_number
    self.sample_size = sample_size
    self.filenames = filenames
    self.directory = os.path.dirname(filenames[0])
    self.new_directory = new_directory
    self.all_ids = set()
    self.sample_ids = set()

  def get_all_ids(self):
    """
    Collect all of the IDs mentioned in this file into our all_ids set.
    """
    try:
      self.all_ids = list(x.strip() for x in open(self.directory + "/all_ids.txt").readlines())
    except:
      for filename in self.filenames:
        with open(filename, 'r') as fh:
          for line in fh.readlines()[1:]:
            self.all_ids.add(line.split(',')[0])
      with open(self.directory + "/all_ids.txt", "w") as fh:
        for each_id in self.all_ids:
          fh.write(each_id + "\n")

  def get_sample_ids(self):
    self.sample_ids = random.sample(self.all_ids, self.sample_size)

  def extract_by_id(self):
    if not os.path.exists(self.new_directory):
      os.makedirs(self.new_directory)
    for incoming_filename in self.filenames:
      outgoing_filename = os.path.basename(incoming_filename)
      with open(incoming_filename, 'r') as read_fh:
        incoming_data = read_fh.readlines()
        headers = incoming_data.pop(0)
        with open(self.new_directory + '/' + outgoing_filename, 'w') as write_fh:
          write_fh.write(headers)
          for line in incoming_data:
            desynpufid = line.split(',')[0]
            if desynpufid in self.sample_ids:
              write_fh.write(line)

def main():
  try:
    sample_number, sample_size, filenames = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3:]
  except:
    return "Usage: %s SET_ID SAMPLE_SIZE CSV_FILES" % sys.argv[0]
  new_directory = "%i-sample-%i" % (sample_number, sample_size)
  s = Synpuf(sample_number, sample_size, filenames, new_directory)
  s.get_all_ids()
  s.get_sample_ids()
  s.extract_by_id()
  return "%i samples stored in %s/." % (sample_size, new_directory)

if __name__ == '__main__':
  print main()
