from pydantic import BaseModel, Field

class User(BaseModel):
    username: str = Field(
        ...,
        min_length=7,
        max_length=7,
        pattern=r'^(?:[dD][pP]|[eE]0)\d{5}$'
    )
    password: str = Field(..., min_length=1)
