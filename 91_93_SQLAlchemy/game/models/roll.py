import datetime
from model_base import ModelBase
import sqlalchemy


class Roll(ModelBase):
    __tablename__ = 'rolls'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    created = sqlalchemy.Column(sqlalchemy.DateTime,
                                default=datetime.datetime.now)
    name = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=False)
