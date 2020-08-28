from application import db
from application.models import Strategys

db.drop_all()
db.create_all()