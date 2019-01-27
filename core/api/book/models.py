from sqlalchemy import Column, Integer, String

from ..common.database import BaseModel
from ..common.serializers import ModelSerializerMixin


class Book(BaseModel, ModelSerializerMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    author = Column(String)
    isbn = Column(Integer)
