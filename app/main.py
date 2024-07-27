from fastapi import FastAPI
from app.models import tables
from app.models.database import engine
from app.routers.room_routes import router as room_router


app = FastAPI()
tables.Base.metadata.create_all(bind=engine)

app.include_router(
    router=room_router,
    prefix='/turamyzba',
    tags=["Turamyzba"]
)
