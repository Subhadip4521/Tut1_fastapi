from typing import Union
from fastapi import APIRouter  # type: ignore
from fastapi import FastAPI, Request  # type: ignore
from fastapi.responses import HTMLResponse  # type: ignore
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi.templating import Jinja2Templates  # type: ignore


note = APIRouter()
templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):  # type: ignore
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append(
            {"id": doc["_id"], "title": doc["title"], "description": doc["description"]}
        )
    return templates.TemplateResponse(
        "index.html", {"request": request, "newDocs": newDocs}
    )


@note.post("/")
async def add_note(request: Request):
    form = await request.form()
    inserted_note = conn.notes.notes.insert_one(dict(form))
    return {"Success": True}
