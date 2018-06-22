import datetime
import sqlalchemy

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from models.model_base import ModelBase



class Move(ModelBase):
    __tablename__ = 'move'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    created = sqlalchemy.Column(sqlalchemy.DateTime,
                                default=datetime.datetime.now, index=True)
    roll_id = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    game_id = sqlalchemy.Column(sqlalchemy.String, index=True)
    roll_number = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    player_id = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    is_winning_play = sqlalchemy.Column(sqlalchemy.Boolean, index=True,
                                        default=False)
