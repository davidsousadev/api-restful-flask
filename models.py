from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(80), nullable=False)

    def to_dict(self):
        return {"id": self.id, "item": self.item}

