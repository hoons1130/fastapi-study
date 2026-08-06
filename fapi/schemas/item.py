from pydantic import BaseModel, ConfigDict

class ItemCreate(BaseModel):
    name:str
    description: str | None = None

class ItemResponse(BaseModel):
    id:int
    name:str
    description: str|None

    model_config=ConfigDict(from_attributes=True)

class ItemUpdate(BaseModel):
    name:str
    description: str | None = None