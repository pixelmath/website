from app.models.email import Email
import uuid

email_dict = dict(
                        guid = str(uuid.uuid4()),
                        name = "Template 4"
                )
email = Email(**email_dict)
db.session.add(email)
db.session.commit()





