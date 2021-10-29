from datetime import datetime

from Backendproj import db, app




class Payer(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    balance=db.Column(db.Integer)
    total_transactions=db.Column(db.Integer)
    transactions = db.relationship('Transaction', backref='actor', lazy=True)

    def __repr__(self):
        return f"Payer('{self.name}', '{self.total_transactions}')"


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    points=db.Column(db.Integer)
    time_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    payer_id=db.Column(db.Integer, db.ForeignKey('payer.id'), nullable=False)

    def __repr__(self):
        return f"Transaction('Points{self.points},Payer{self.actor.name}', Timestamp'{self.time_posted}')"