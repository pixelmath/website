from app.models.email import Email
import uuid

social_campaign_dict = dict(
                        guid = str(uuid.uuid4()),
                        name = "Social Campaign"
                )
social_campaign = Email(**social_campaign_dict)
db.session.add(social_campaign)
db.session.commit()





