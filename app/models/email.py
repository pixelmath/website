from app import db
from flask import current_app
import uuid
import datetime

class Email(db.Model):
    __tablename__ = "email"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    guid = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    open_email = db.relationship('OpenEmailLog', lazy=True, backref="email")
    visit_website = db.relationship('VisitWebsiteLog', lazy=True, backref="email")

class OpenEmailLog(db.Model):
    __tablename__ = "open_email_log"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    guid = db.Column(db.String, unique=True, nullable=False)
    opened_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    email_id = db.Column(db.Integer, db.ForeignKey('email.id'), nullable=False)

    @staticmethod
    def log_open(email_id):
        open_email_log = OpenEmailLog(
                                            guid = str(uuid.uuid4()),
                                            email_id = email_id
                                    )
        db.session.add(open_email_log)
        db.session.commit()

class VisitWebsiteLog(db.Model):
    __tablename__ = "visit_website_log"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    guid = db.Column(db.String, unique=True, nullable=False)
    visited_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    email_id = db.Column(db.Integer, db.ForeignKey('email.id'), nullable=False)

    @staticmethod
    def log_visit(email_id):
        visit_website_log = VisitWebsiteLog(
                                                guid = str(uuid.uuid4()),
                                                email_id = email_id
                                        )
        db.session.add(visit_website_log)
        db.session.commit()
