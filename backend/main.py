from fastapi import FastAPI
from ethereum.router import user

app = FastAPI()
app.include_router(user.router)
