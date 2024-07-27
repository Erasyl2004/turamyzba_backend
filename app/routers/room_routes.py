from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from app.models import tables
from app.models.database import get_db
from app.models.schemas import RoommatesCreate, Roommates,RoomCreate, Room
from app.ai_controllers.preferences import get_preference
from app.controllers.room_controllers import get_room_id,find_roommates,delete_roommate

router = APIRouter()

@router.post("/add_roommate")
async def create_roommate(roommate: RoommatesCreate, db: Session = Depends(get_db)):
    preference = get_preference(roommate.preference)
    room_id = get_room_id(roommate.personality_type)
    
    db_roommate = tables.Roommates(
        user_id=roommate.user_id,
        room_id=room_id,
        user_name=roommate.user_name,
        personality_type=roommate.personality_type,
        preference=preference,
        gender=roommate.gender,
        location=roommate.location,
        age=roommate.age,
        start_money_range=roommate.start_money_range,
        end_money_range=roommate.end_money_range
    )
    db.add(db_roommate)
    db.commit()
    db.refresh(db_roommate)
    return db_roommate

@router.get("/potential_roommates", response_model=List[Roommates])
async def get_potential_roommates(user_id: int, db: Session = Depends(get_db)):
    roommates = find_roommates(user_id,db)
    return roommates


@router.delete("/delete_roommate")
async def remove_roommate(user_id: int, db: Session = Depends(get_db)):
    result = delete_roommate(user_id, db)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result

@router.post("/add_room", response_model=Room)
async def create_room(room: RoomCreate, db: Session = Depends(get_db)):
    db_room = tables.Room(
        room_preferences=room.room_preferences
    )
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room