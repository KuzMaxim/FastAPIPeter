from persistent.db.base import Base
from sqlalchemy import  Column, Text
import uuid

def uuid4_as_str()->str:
    return str(uuid.uuid4())

class Link(Base):
    __tablename__ = "link"
    id = Column(Text, default = uuid4_as_str, primary_key=True)
    
    short_link = Column(Text, nullable = False, unique = True)
    long_link = Column(Text, nullable = False)
