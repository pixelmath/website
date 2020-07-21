from app import db
import datetime
import uuid

class Referral(db.Model):
    __tablename__ = "referral_registrations"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    guid = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    mobile_number = db.Column(db.String, nullable=False)
    grade = db.Column(db.String, nullable=False)
    referral_id = db.Column(db.String)
    registered_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def to_json(self):
        return {
                    "id": self.id,
                    "guid": self.guid,
                    "name": self.name,
                    "email": self.email,
                    "mobile_number": self.mobile_number,
                    "grade": self.grade,
                    "referral_id": self.referral_id,
                    "registered_at": self.registered_at
            }

    @staticmethod
    def save(name, email, mobile_number, grade, referral_id):
        referral = Referral(
                            guid = str(uuid.uuid4()),
                            name = name,
                            email = email,
                            mobile_number = mobile_number,
                            grade = grade,
                            referral_id = referral_id
                    )
        db.session.add(referral)
        db.session.commit()
        return referral
