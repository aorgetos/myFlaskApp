# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from flask import Blueprint

vocabulary = Blueprint('vocabulary', __name__)

from . import views