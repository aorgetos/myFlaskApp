#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import os, logging

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
  

from appl import app as application
logging.basicConfig(stream = sys.stderr)