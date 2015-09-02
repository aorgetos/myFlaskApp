# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function
from flask import render_template

from flask.ext.login import current_user, login_required

from . import main
from .. import login_man
from ..models import VocabItem, User


# --------------------------------------------------------
@login_man.user_loader
def load_user(userid):
    return User.query.get(int(userid))

# --------------------------------------------------------
@main.route('/index')
@main.route('/')
#@login_required
def index():
    return render_template('index.html', new_words = VocabItem.allRecords())

# --------------------------------------------------------
@main.app_errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@main.app_errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403
