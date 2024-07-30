from fastapi import FastAPI, status, Depends, HTTPException
from db.models import TheBoys, engine
from sqlmodel import Session, select

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hola Mundo!"}


@app.get("/characters")
async def get_characters(limit: int = None):

    with Session(engine) as session:
        statement = select(TheBoys)
        if limit != None:
            results = session.exec(statement).fetchmany(limit)
        else:
            results = session.exec(statement).all()
        
        res = [i for i in results]

        return res
        
        # return {"results": res}


@app.post("/characters")
async def upload_characters(name: str, full_name: str, description: str,
                            image_url: str, actor_name: str, gender: str):

    character = TheBoys(name=name, full_name=full_name, description=description,
                        image_url=image_url, actor_name=actor_name, gender=gender)

    with Session(engine) as session:
        session.add(character)
        session.commit()
        return {"message": "Success"}

