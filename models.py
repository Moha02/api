from blog.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key= True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    
    createdBy = relationship("User", back_populates="blogs")
    
class User(Base):
    
    __tablename__ = 'user'
    id = Column(Integer, primary_key= True, index=True)
    name = Column(String, unique=True,)
    email = Column(String, unique=True)
    password = Column(String)
    
    
    blogs = relationship("Blog", back_populates= "createdBy")
    
    