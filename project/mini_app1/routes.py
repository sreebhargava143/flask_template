from flask import render_template, url_for, current_app, redirect, session, flash

from project.mini_app1 import mini_app1_bp
from project.mini_app1.forms import TestForm

@mini_app1_bp.route("/", methods=["GET", "POST"])
def index():
    form = TestForm()
    if form.validate_on_submit():
        flash("form valid", "success")
        return redirect(url_for("mini_app1.index"))

    return render_template("index.html", form=form)
