from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from db.models import TheBoys, engine
from sqlmodel import Session, select
import os

app = FastAPI()

origins = os.getenv("ORIGIN_URL")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    """See if the API is alive"""
    return {"message" : "Hello World!"}


@app.get("/characters", response_model=list[TheBoys])
async def get_characters(skip: int = None, limit: int = None):
    """Get all characters of the database"""
    with Session(engine) as session:
        statement = select(TheBoys)
        if skip is not None or limit is not None:
            results = session.exec(statement.offset(skip).limit(limit))
        else:
            results = session.exec(statement).all()

        res = [i for i in results]
        return res

@app.get("/characters/{character_id}", response_model=TheBoys)
async def get_character_by_id(character_id: int):
    """Filter character by ID"""
    with Session(engine) as session:
        character = session.get(TheBoys, character_id)
        if not character:
            raise HTTPException(404, "Character not found")
        return character


############################
# Only for development use #
############################
@app.post("/characters", status_code=status.HTTP_201_CREATED, response_model=TheBoys)
async def upload_characters(character: TheBoys):
    """Insert Characters into the database"""
    
    characters = TheBoys(name=character.name, full_name=character.full_name, description=character.description,
                        image_url=character.image_url, actor_name=character.actor_name, gender=character.gender)

    with Session(engine) as session:
        session.add(characters)
        session.commit()
        return {"message" : "Character created succesfully"}

@app.put("/characters/{character_id}", response_model=TheBoys)
async def update_character_info(character_id: int, character: TheBoys):
    """Update character info by ID"""
    
    with Session(engine) as session:
        db_character = session.get(TheBoys, character_id)
        if not db_character:
            raise HTTPException(404, "Character not found")
        
        character_data = character.model_dump(exclude_unset=True)
        db_character.sqlmodel_update(character_data)
        session.add(db_character)
        session.commit()
        session.refresh(db_character)
    return db_character

@app.delete("/characters/{character_id}")
async def delete_character(character_id: int):
    """Delete character by ID"""
    
    with Session(engine) as session:
        db_character = session.get(TheBoys, character_id)
        if not db_character:
            raise HTTPException(404, "Character not found")
        
        session.delete(db_character)
        session.commit()
        return {"message" : "Character deleted from db succesfully"}
    