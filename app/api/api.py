from flask import Blueprint, jsonify, request, render_template, redirect, session, url_for
from app.models.signup import Signup
from app import db
from app.models.email import Email, OpenEmailLog

api = Blueprint('api', __name__, url_prefix="/api")

@api.route('/signup', methods=["POST"])
def signup():
    signup = Signup.save(**request.json)
    return jsonify({}), 201

@api.route('/email-open')
def email_open():
    email_guid = request.args.get("guid")
    email = Email.query.filter_by(guid=email_guid).first()
    if email:
        OpenEmailLog.log_open(email.id)
    return jsonify({}), 200
