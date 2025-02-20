from datetime import datetime
from pydantic import BaseModel


class News(BaseModel):
    title: str
    dateTime: datetime
    description: str
    image: str
