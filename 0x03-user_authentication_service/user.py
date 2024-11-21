#!/usr/bin/env python3

"""
user model module
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


# Create a declarative base
Base = declarative_base()


class User(Base):
    """User model
     Args:
        Base (class): declarative base from sqlalchemy
    """
    __tablename__ = 'users'

    # Define columns
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
