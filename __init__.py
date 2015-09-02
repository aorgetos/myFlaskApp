# -*- coding: utf-8 -*-

import os
from vocab import create_app


app = create_app(os.getenv('VOCAB_ENV') or 'prod')