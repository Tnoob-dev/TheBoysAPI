from fastapi import FastAPI
from db.models import TheBoys, engine
from sqlmodel import Session, select


app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello World!"}


@app.get("/characters")
async def get_characters(skip: int = None, limit: int = None):

    with Session(engine) as session:
        statement = select(TheBoys)
        if skip != None or limit != None:
            results = session.exec(statement.offset(skip).limit(limit))
        else:
            results = session.exec(statement).all()

        res = [i for i in results]
        return res


############################
# Only for development use #
############################
# @app.post("/characters")
# async def upload_characters(name: str, full_name: str, description: str,
#                             image_url: str, actor_name: str, gender: str):

#     character = TheBoys(name=name, full_name=full_name, description=description,
#                         image_url=image_url, actor_name=actor_name, gender=gender)

#     with Session(engine) as session:
#         session.add(character)
#         session.commit()
#         return {"message": "Success"}