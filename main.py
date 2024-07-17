'''
Command to run - fastapi dev main.py (for development) or
                uvicorn main:app --reload (reload is for updating the changes quickly)
                fastapi run (for production server)


'''


from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
async def root():
    return {"message": "Hello world!!!"}

@app.get("/posts")
def get_posts():
    return {"data": " This is your posts!"}


@app.post("/createpost")
def create_posts(new_post: Post):
    print(new_post)
    return {"data": "new post"}


