from app import db


# Add all the tables, eg Assessments and all the properties for it
class Assessments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    assessmenttitle = db.Column(db.String(500), index=True)
    modulecode = db.Column(db.String(100), index=True)
    deadline = db.Column(db.Date)
    description = db.Column(db.Text)
    status = db.Column(db.Boolean, default=False)
