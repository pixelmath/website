from flask import Blueprint, jsonify, request, render_template, redirect, session, url_for
from app.models.signup import Signup
from app import db

main = Blueprint('main', __name__, url_prefix="/")

@main.route('/')
def index():
    return render_template("/index.html")

@main.route('/blog')
def blog():
    return render_template("/blog.html")

@main.route('/scanner')
def scanner():
    return render_template("/scanner.html")