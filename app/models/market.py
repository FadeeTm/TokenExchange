from app import db


class Market(db.Model):
    __tablename__ = 'Market'


    id = db.column(db.Integer, primary_key=True)
    name = db.column(db.String(50), nullable=False)


    def __repr__(self):
        return '<Market %r>' % self.id