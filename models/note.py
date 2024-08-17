from pydantic import BaseModel # type: ignore


class Note(BaseModel):
    note: str
    description: str