from flask import Blueprint, jsonify, request, render_template, redirect, session, url_for
from app.models.signup import Signup
from app import db
from app.models.email import Email, VisitWebsiteLog

main = Blueprint('main', __name__, url_prefix="/")

@main.route('/')
def index():
    email_guid = request.args.get("guid")
    from_email = request.args.get("email")
    email = Email.query.filter_by(guid=email_guid).first()
    if email:
        already_logged = VisitWebsiteLog.query.filter_by(email_id=email.id, from_email=from_email).first()
        if not already_logged:
            VisitWebsiteLog.log_visit(email.id, from_email)
    return render_template("/index.html")

@main.route('/blog')
def blog():
    return render_template("/blog.html")

@main.route('/scanner')
def scanner():
    return render_template("/scanner.html")
