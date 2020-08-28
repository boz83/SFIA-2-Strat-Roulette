from application import db

class Strategys(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  map = db.Column(db.String(30), nullable=False)
  strategy = db.Column(db.String(30), nullable=False)
  rule = db.Column(db.String(1000), nullable=False)