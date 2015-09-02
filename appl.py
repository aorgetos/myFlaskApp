#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
from vocab import create_app


app = create_app(os.getenv('VOCAB_ENV') or 'prod')

# Partie pour l'excecution
if __name__ == '__main__':
    app.run()
  