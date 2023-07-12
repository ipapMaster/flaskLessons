import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    name = sqlalchemy.column(sqlalchemy.String, nullable=True)
    about = sqlalchemy.column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.column(sqlalchemy.String, index=True,
                              unique=True, nullable=True)
    hashed_password = sqlalchemy.column(sqlalchemy.String, nullable=True)
    create_date = sqlalchemy.column(sqlalchemy.DateTime,
                                    default=datetime.datetime.now())