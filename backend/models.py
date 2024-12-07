from typing import Optional

from pydantic import BaseModel, Field


class Feedback(BaseModel):
    token: str = Field(min_length=1)
    name: str = Field(min_length=3, max_length=25)
    phone: str = Field(min_length=11, max_length=11)
    email: Optional[str] = Field(default=None, min_length=5, max_length=20)
    msg: str = Field(min_length=10, max_length=2000)
    status_publish


class SignForm(BaseModel):
    token: str = Field(min_length=1)
    name: str = Field(min_length=3, max_length=25)
    phone: str = Field(min_length=11, max_length=11)
