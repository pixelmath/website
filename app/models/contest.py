from app import db
import datetime
import uuid

class Contest(db.Model):
    __tablename__ = "contest_registrations"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    guid = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    mobile_number = db.Column(db.String, nullable=False)
    grade = db.Column(db.String, nullable=False)
    registered_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    @staticmethod
    def save(name, email, mobile_number, grade):
        contest = Contest(
                            guid = str(uuid.uuid4()),
                            name = name,
                            email = email,
                            mobile_number = mobile_number,
                            grade = grade
                    )
        db.session.add(contest)
        db.session.commit()
        return contest
