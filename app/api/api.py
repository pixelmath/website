from flask import Blueprint, jsonify, request, render_template, redirect, session, url_for
from app.models.signup import Signup
from app import db

api = Blueprint('api', __name__, url_prefix="/api")

@api.route('/signup', methods=["POST"])
def signup():
    signup = Signup.save(**request.json)
    return jsonify({}), 201
