from app import db
import datetime
from sqlalchemy.orm import validates
from flask import current_app
import uuid
from app.models.email import Email

class Signup(db.Model):
    __tablename__ = "signup"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    guid = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    grade = db.Column(db.String, nullable=False)
    email_campaign_id = db.Column(db.Integer, db.ForeignKey('email.id'))
    country_code = db.Column(db.String, nullable=False)
    mobile = db.Column(db.String, nullable=False)
    signup_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    @staticmethod
    def save(**kwargs):
        email_campaign = Email.query.filter_by(guid=kwargs.get("email_campaign")).first() or ""
        email_campaign_id = None
        if email_campaign:
            email_campaign_id = email_campaign.id
        signup = Signup(
                            guid = str(uuid.uuid4()),
                            name = kwargs.get("name"),
                            grade = kwargs.get("grade"),
                            email_campaign_id = email_campaign_id,
                            country_code = kwargs.get("country_code"),
                            mobile = kwargs.get("mobile")
                    )
        db.session.add(signup)
        db.session.commit()
        return signup
