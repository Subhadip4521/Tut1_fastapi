from fastapi import FastAPI # type: ignore
from routes.note import note
from fastapi.staticfiles import StaticFiles  # type: ignore

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(note)
