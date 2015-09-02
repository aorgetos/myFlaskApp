#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function
import os
from vocab import create_app, db
from flask.ext.script import Manager, prompt_bool
from vocab.models import User, VocabItem
from flask.ext.migrate import Migrate, MigrateCommand

########################################################################

app = create_app(os.getenv('VOCAB_ENV') or 'prod')
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def initdb():
    #db.create_all()
    User.register("robertas", "heidrich")
    print("Initialized the database")

@manager.command
def dropdb():
    if prompt_bool("Are you sure you want to lose all your data?"):
        db.drop_all()
        print("Dropped the database")
    
# Partie pour l'excecution
if __name__ == '__main__':
    manager.run()
  