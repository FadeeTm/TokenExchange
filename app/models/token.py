from app import db


class Token(db.Model):
    __tablename__ = 'Token'


    id = db.column(db.Integer, primary_key=True)
    name = db.column(db.String(50), nullable=False)


    def __repr__(self):
        return '<Token %r>' % self.id