from app import db
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ARRAY, Column, Date, Float, ForeignKey, Integer, String
from datetime import datetime

class Cost(db.Model):
    __tablename__ = 'Cost'


    id = db.column(db.Integer, primary_key=True)
    token1_id = Column(ForeignKey('Token.id'), nullable=False, index=True)
    token2_id = Column(ForeignKey('Token.id'), nullable=False, index=True)
    market_id = Column(ForeignKey('Market.id'), nullable=False, index=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    cost = db.column(db.Double, nullable=False)


    def __repr__(self):
        return '<Token %r>' % self.id