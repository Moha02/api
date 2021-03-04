from fastapi import FastAPI, Depends, status, Response, HTTPException
from blog import schemas, models
# import .models
import uvicorn
from blog.database import engine


from .routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

