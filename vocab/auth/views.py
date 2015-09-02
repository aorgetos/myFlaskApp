# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function
from flask import render_template, url_for, request, redirect
from flask import flash
from flask.ext.login import login_required, login_user, logout_user
from flask.ext.login import current_user

from . import auth
from .. import db
from ..models import User
from .forms import LoginForm, SignupForm

# --------------------------------------------------------
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # login and validate user ...
        user = User.get_by_username(form.username.data)
        if user is None or not user.verify_password(form.password.data):
            flash("Incorrect user name or password.", "alert-danger")
            return redirect(url_for('.login', **request.args))
        login_user(user, form.remember_me.data)
        flash("Logged in successfully as {}".format(user.username), "alert-success")
        return redirect(request.args.get('next') or url_for('main.index'))
    return render_template('login.html', form = form)


# --------------------------------------------------------
@auth.route('/singup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        name = form.username.data.strip()
        User.register(name, form.password.data )
        flash("Hello {}! Please, logg in.".format(name), "alert-success")
        return redirect(url_for('.login'))
    return render_template('signup.html', form = form)


# --------------------------------------------------------
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "alert-success")
    return redirect(url_for('main.index'))
