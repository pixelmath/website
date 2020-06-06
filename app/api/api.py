from flask import Blueprint, jsonify, request, render_template, redirect, session, url_for
from app.models.signup import Signup
from app import db
from app.models.email import Email, OpenEmailLog
from app.models.contest import Contest
from app.utils.contest_util import validate_email
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
