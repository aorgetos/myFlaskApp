# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Required, Length, DataRequired, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


# ================================================================   
class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(3, 80),
                                                   Regexp('^[A-Za-z]{3,}$', 
                                                            flags=0, 
                                                            message="Username must have only letters")])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Log In')
    

# ================================================================      
class SignupForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(3, 80),
                                                   Regexp('^[A-Za-z]{3,}$', 
                                                            flags=0, 
                                                            message="Username must have only letters")])
    password = PasswordField('Password', validators=[Required(),
                                                     EqualTo("password2", 
                                                            message="Passwords must match.")])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Log In')
    
    
    def validate_username(self, field):
        name = field.data.strip().lower()
        if User.query.filter_by(username = name).first():
            raise ValidationError("Name '{}' is already taken".format(name))
        
        
    def validate(self):        
        if not Form.validate(self):
            return False
    
        self.username.data = self.username.data.strip()
        return True    