from flask import Blueprint, jsonify, request, render_template, redirect, session, url_for
from app.models.signup import Signup
from app import db
from app.models.email import Email, OpenEmailLog
from app.models.contest import Contest
from app.models.referral import Referral
from app.utils.contest_util import validate_email
from app.utils.mailer import send_mail
import os

api = Blueprint('api', __name__, url_prefix="/api")

@api.route('/signup', methods=["POST"])
def signup():
    signup = Signup.save(**request.json)
    return jsonify({}), 201

@api.route("/contest-registration", methods=["POST"])
def contest_registration():
    name = request.json.get("name")
    email = request.json.get("email")
    mobile_number = request.json.get("mobile_number")
    grade = request.json.get("grade")
    if not all((name, email, mobile_number, grade)):
        return jsonify({
            "message": "All Fields are required!",
            "status": "error"
        }), 400
    if not validate_email(email):
        return jsonify({
            "message": "Invalid Email Address!",
            "status": "error"
        }), 400
    contest = Contest.save(name, email, mobile_number, grade)
    # try:
    #     send_mail(email)
    return jsonify({}), 201
    # except Exception as e:
    #     return jsonify({
    #         "message": "Please check if the email address is correct and try again.",
    #         "status": "Error"
    #     }), 400

@api.route("/referral-registration", methods=["POST"])
def referral_registration():
    name = request.json.get("name")
    email = request.json.get("email")
    mobile_number = request.json.get("mobile_number")
    grade = request.json.get("grade")
    referral_id = request.json.get("referral_id")
    if not all((name, email, mobile_number, grade)):
        return jsonify({
            "message": "All Fields are required!",
            "status": "error"
        }), 400
    if not validate_email(email):
        return jsonify({
            "message": "Invalid Email Address!",
            "status": "error"
        }), 400
    referral = Referral.save(name, email, mobile_number, grade, referral_id)
    return jsonify({}), 201

@api.route("/get-contest-entries")
def get_contest_entries():
    unique_id = request.args.get("uid")
    if unique_id != os.environ.get("unique_id"):
        return jsonify({
            "message": "Invalid Unique ID",
            "status": "error"
        }), 400
    return_json = [contest.to_json() for contest in Contest.query.all()]
    return jsonify({
                        "data": return_json,
                        "status": "success"
                }), 200

@api.route("/get-referral-entries")
def get_referral_entries():
    unique_id = request.args.get("uid")
    if unique_id != os.environ.get("unique_id"):
        return jsonify({
            "message": "Invalid Unique ID",
            "status": "error"
        }), 400
    referral_id = request.args.get("referral_id")
    if referral_id:
        referrals = Referral.query.filter_by(referral_id=referral_id).all()
    else:
        referrals = Referral.query.all()
    return_json = [referral.to_json() for referral in referrals]
    return jsonify({
                        "data": return_json,
                        "status": "success"
                }), 200
