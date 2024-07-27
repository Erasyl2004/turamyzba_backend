from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.models import tables
from app.models.schemas import Roommates
from fastapi import HTTPException
from typing import List

def get_room_id(personality_type: str):
    if(personality_type in "ISTJ,ESTJ,ISFJ,INTJ"):
        return 1
    elif(personality_type in "INFJ,ENFJ,INFP,ENFP"):
        return 2
    elif(personality_type in "ISTP,ESTP,INTP,ENTP"):
        return 3
    elif(personality_type in "ISFP,ESFP,ENTJ,ESFJ"):
        return 4
    else:
        return 0

def find_roommates(user_id: int, db: Session) -> List[Roommates]:
    user = db.query(tables.Roommates).filter(tables.Roommates.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    potential_roommates = db.query(tables.Roommates).filter(
        tables.Roommates.room_id == user.room_id,
        tables.Roommates.user_id != user_id, 
        tables.Roommates.preference == user.preference,
        tables.Roommates.gender == user.gender,
        tables.Roommates.age.between(user.age - 3, user.age + 3),
        and_(
            tables.Roommates.start_money_range <= user.end_money_range,
            tables.Roommates.end_money_range >= user.start_money_range
        )
    ).all()

    return potential_roommates

def delete_roommate(user_id: int, db: Session):
    roommate = db.query(tables.Roommates).filter(tables.Roommates.user_id == user_id).first()
    if not roommate:
        return {"error": "Roommate not found"}

    db.delete(roommate)
    db.commit()
    return {"message": "Roommate deleted successfully"}