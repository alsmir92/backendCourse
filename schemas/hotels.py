from pydantic import BaseModel, Field


class Hotel(BaseModel):  # pydantic схема
    title: str | None = Field(None)
    name: str | None = Field(None)


class HotelPATCH(BaseModel):
    title: str | None = Field(None)
    name: str | None = Field(None)
