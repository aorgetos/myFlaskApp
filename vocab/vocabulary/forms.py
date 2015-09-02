# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required, Length
from wtforms import ValidationError
from ..models import VocabItem


# =====================================================================
class AddWordForm(Form):
    word = StringField('Mot', validators = [Required(), Length(1, 100)])
    translation = StringField('Traduction', validators = [Required()])
    note = TextAreaField('Note')
    submit = SubmitField('Submit')
    edit = False
    
    def __init__(self, **kwargs):
        self.edit = kwargs.get("edit", False)
        Form.__init__(self, **kwargs)
    
    def validate_word(self, field):
        mot = field.data.strip().lower()
        if not self.edit and VocabItem.query.filter_by(word = mot).first():
            raise ValidationError("Word '{}' already in the database".format(mot))
        
    def validate(self):        
        if not Form.validate(self):
            return False
        
        self.word.data = self.word.data.strip().lower()
        self.translation.data = self.translation.data.strip().lower()

        return True
        