#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os, sys
#sys.path.insert(0, '/var/www/html/widget_corp/vocab/')
#sys.path.append("/var/www/html/widget_corp/vocab/")
#print ("{}".format(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ..vocab import create_app




app = vocab.create_app(os.getenv('VOCAB_ENV') or 'prod')

# Partie pour l'excecution
if __name__ == '__main__':
    app.run()
  