from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {"title": "Title 1", "content": "content of post 1", "id": 1},
    {"title": "Favorite Candies", "content": "I like jujuba", "id": 2},
]


@app.get("/")
async def root():
    return {"Message": "Welcome to my api"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts")
def create_post(post: Post = Body(...)):
    post_dict = post.dict()
    post_dict["id"] = randrange(1, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts) - 1]
    return {"detail": post}


@app.get("/posts/{id}")
def get_post(id: int):
    post_by_id = list(filter(lambda post: post["id"] == id, my_posts))
    return {"post_detail": f"here is post {post_by_id[0]}"}
