# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function
from flask import render_template, url_for, request, redirect
from flask import flash
from flask.ext.login import current_user, login_required

from . import vocabulary
from .. import db
from ..models import User, VocabItem
from .forms import AddWordForm


# flash params:
# alert-danger
# alert-warning
# alert-info
# alert-success


# --------------------------------------------------------
@vocabulary.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    word = None
    form = AddWordForm()
    if form.validate_on_submit():
        new_item = VocabItem(word = form.word.data, translation = form.translation.data, note = form.note.data)
        db.session.add(new_item)
        db.session.commit()
        flash("New word entered: '{}'".format(form.word.data), "alert-info")
        return redirect(url_for("main.index"))
    return render_template('add_form.html', form = form, title = "Add a new word")


# --------------------------------------------------------
@vocabulary.route('/edit/<int:entry_id>', methods=['GET', 'POST'])
@login_required
def edit_word(entry_id):
    eword = VocabItem.query.get_or_404(entry_id)
    form = AddWordForm(obj = eword, edit = True)
    if form.validate_on_submit():
        # form.populate_obj(eword)
        eword.translation = form.translation.data
        eword.note = form.note.data
                        
        db.session.commit()
        flash("Stored '{}'".format(eword.word), "alert-info")
        return redirect(url_for("main.index"))
    return render_template('add_form.html', form = form, title = "Edit entry", edit = True)


# --------------------------------------------------------
@vocabulary.route('/delete/<int:entry_id>', methods=['GET', 'POST'])
@login_required
def delete_word(entry_id):
    eword = VocabItem.query.get_or_404(entry_id)
    if request.method == "POST":
        db.session.delete(eword)                        
        db.session.commit()
        flash("Deleted '{}'".format(eword.word), "alert-info")
        return redirect(url_for("main.index"))
    else:
        flash("Please confirm deleting the word", "alert-warning")   
    return render_template('confirm_delete.html', title = "Delete entry")
