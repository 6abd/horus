import os
import pytest
import sys
 
# setting path
sys.path.append('../horus')
import horus

def test_horus():
  os.system('python3 horus.py')
