from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from db.models import TheBoys, Episodes, engine
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
    return {"message": "Hello World!"}


@app.get("/characters")
async def get_characters(skip: int = None, limit: int = None):
    """Get all characters of the database"""
    with Session(engine) as session:
        statement = select(TheBoys)
        if skip is not None or limit is not None:
            results = session.exec(statement.offset(skip).limit(limit))
        else:
            results = session.exec(statement).all()

        res = [i for i in results]
        return {"results": res}


@app.get("/characters/{character_id}")
async def get_character_by_id(character_id: int):
    """Filter character by ID"""
    with Session(engine) as session:
        character = session.get(TheBoys, character_id)
        if not character:
            raise HTTPException(404, "Character not found")
        return character

@app.get("/episodes")
async def get_episodes(skip: int = None, limit: int = None):
    """Get all episodes of the database"""
    with Session(engine) as session:
        statement = select(Episodes)
        if skip is not None or limit is not None:
            results = session.exec(statement.offset(skip).limit(limit))
        else:
            results = session.exec(statement).all()
        
        res = [i for i in results]
        return {"results": res}

@app.get("/episodes/{episode_id}")
async def get_episode_by_id(episode_id: int):
    """Filter episode by ID"""
    with Session(engine) as session:
        episode = session.get(Episodes, episode_id)
        if not episode:
            raise HTTPException(404, "Episode not found")
        return episode


############################
# Only for development use #
############################
@app.post("/characters", status_code=status.HTTP_201_CREATED)
async def upload_characters(character: TheBoys):
    """Insert Characters into the database"""

    characters = TheBoys(name=character.name, full_name=character.full_name, description=character.description,
                         image_url=character.image_url, actor_name=character.actor_name, gender=character.gender)

    with Session(engine) as session:
        session.add(characters)
        session.commit()
        return {"message": "Character created succesfully"}


@app.put("/characters/{character_id}")
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
        return {"message": "Character deleted from db succesfully"}

@app.post("/episodes", status_code=status.HTTP_201_CREATED)
async def upload_episodes(ep_name: str, season: str, description: str):
    """Insert Episodes into the database"""
    
    episodes = Episodes(ep_name=ep_name, season=season, description=description)
    with Session(engine) as session:
        session.add(episodes)
        session.commit()
        return {"message": "Episode created succesfully"}

@app.delete("/episodes/{episode_id}")
async def delete_episodes(episode_id: int):
    """Delete episode by ID"""
    
    with Session(engine) as session:
        db_episode = session.get(Episodes, episode_id)
        if not db_episode:
            raise HTTPException(404, "Episode not found")
        
        session.delete(db_episode)
        session.commit()
        
        return {"message" : "Episode deleted from db succesfully"}
    