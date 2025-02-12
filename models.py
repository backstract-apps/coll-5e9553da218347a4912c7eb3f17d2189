from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import class_mapper
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, \
    TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base


@as_declarative()
class Base:
    id: int
    __name__: str

    # Auto-generate table name if not provided
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # Generic to_dict() method
    def to_dict(self):
        """
        Converts the SQLAlchemy model instance to a dictionary, ensuring UUID fields are converted to strings.
        """
        result = {}
        for column in class_mapper(self.__class__).columns:
            value = getattr(self, column.key)
                # Handle UUID fields
            if isinstance(value, uuid.UUID):
                value = str(value)
            # Handle datetime fields
            elif isinstance(value, datetime):
                value = value.isoformat()  # Convert to ISO 8601 string
            # Handle Decimal fields
            elif isinstance(value, Decimal):
                value = float(value)

            result[column.key] = value
        return result




class Users(Base):
    __tablename__ = 'users'
    id = Column(UUID, primary_key=True)
    username = Column(String, primary_key=False)
    name = Column(String, primary_key=False)
    email = Column(String, primary_key=False)
    password = Column(String, primary_key=False)
    created_at = Column(Time, primary_key=False)
    token = Column(String, primary_key=False)
    updated_at = Column(Time, primary_key=False)


class Assignees(Base):
    __tablename__ = 'assignees'
    id = Column(Integer, primary_key=True)
    created_at = Column(Time, primary_key=False)
    updated_at = Column(Time, primary_key=False)
    task_id = Column(Integer, primary_key=False)
    team_id = Column(Integer, primary_key=False)
    user_id = Column(UUID, primary_key=False)
    user_name = Column(String, primary_key=False)


class Tasks(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    created_at = Column(Time, primary_key=False)
    updated_at = Column(Time, primary_key=False)
    task_id = Column(String, primary_key=False)
    task_name = Column(String, primary_key=False)
    ask_description = Column(String, primary_key=False)
    priority = Column(String, primary_key=False)
    visibility = Column(String, primary_key=False)
    tags = Column(String, primary_key=False)


class Team(Base):
    __tablename__ = 'team'
    id = Column(Integer, primary_key=True)
    created_at = Column(Time, primary_key=False)
    team_name = Column(String, primary_key=False)
    limit = Column(Integer, primary_key=False)


class TeamUsers(Base):
    __tablename__ = 'team_users'
    team_id = Column(Integer, primary_key=False)
    user_id = Column(UUID, primary_key=False)
    can_view = Column(String, primary_key=False)
    can_comment = Column(String, primary_key=False)
    can_edit = Column(String, primary_key=False)
    created_at = Column(Time, primary_key=False)
    id = Column(Integer, primary_key=True)


