from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from app.models.database import Base
from sqlalchemy.orm import relationship

class Roommates(Base):
    __tablename__ = 'roommates'
    
    user_id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey('room.room_id'), primary_key=True, index=True)
    user_name = Column(String, index=True)
    personality_type = Column(String, index=True)
    preference = Column(String, index=True)
    gender = Column(Boolean, index=True)
    location = Column(String, index=True)
    age = Column(Integer, index=True)
    start_money_range = Column(Integer, index=True)
    end_money_range = Column(Integer, index=True)

    room = relationship("Room", back_populates="roommates")

class Room(Base):
    __tablename__ = 'room'
    
    room_id = Column(Integer, primary_key=True, index=True)
    room_preferences = Column(String, index=True)

    roommates = relationship("Roommates", back_populates="room")
