from pydantic import BaseModel
from typing import List

class RoommatesBase(BaseModel):
    user_id: int
    user_name: str
    personality_type: str
    preference: str
    gender: bool
    location: str
    age: int
    start_money_range: int
    end_money_range: int

class RoommatesCreate(RoommatesBase):
    pass

class Roommates(RoommatesBase):
    room_id: int

    class Config:
        orm_mode = True
