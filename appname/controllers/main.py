from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy.exc import SQLAlchemyError

from appname import cache
from appname.forms import LoginForm, SignupForm, ChangePasswordForm
from appname.models import User

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
@cache.cached(timeout=1000)
def home():
    return render_template('index.html')


@main_bp.route('/health/')
def health():
    return "OK"


@main_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.authenticate(username=form.username.data,
                                 password=form.password.data)
        if user and login_user(user):
            flash("Logged in successfully.", "success")
            return redirect(request.args.get("next") or url_for(".home"))
        else:
            flash("Login failed.", "danger")

    return render_template("login.html", form=form)


@main_bp.route("/changepass", methods=["GET", "POST"])
@login_required
def change_password():
    form = ChangePasswordForm()
    if request.method == "GET":
        return render_template("change_password.html", form=form)

    # Re-validate old password
    if form.validate_on_submit() and User.authenticate(
            current_user.username, form.current_password.data):
        current_user.update_password(form.password.data)
        current_user.save()
        flash("Password change successfully.", "success")
        return redirect(url_for(".home"))
    else:
        flash("Password change failed.", "danger")
        return render_template("change_password.html", form=form)


@main_bp.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for(".home"))


@main_bp.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        try:
            user = User(username=form.username.data,
                        password=form.password.data).save()
        except SQLAlchemyError:
            user = None
            
        if user:
            login_user(user)
            flash("Account created successfully.", "success")
            return redirect(request.args.get("next") or url_for(".home"))
        else:
            flash("Account creation failed.", "danger")

    return render_template("signup.html", form=form)
