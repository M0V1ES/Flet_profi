from datetime import datetime
from pydantic import BaseModel


class Events(BaseModel):
    title: str
    dateTime: datetime
    author: str
    description: str
