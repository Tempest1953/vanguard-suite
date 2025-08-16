from pydantic import BaseModel, Field
from typing import Optional, Literal
class Contact(BaseModel):
    id: str; company_id: str; name: str; email: str
    title: Optional[str]=None; region: Optional[str]=None
    status: Optional[Literal['new','engaged','positive','negative','booked']]='new'
    opt_out: bool=False
class Company(BaseModel):
    id: str; name: str; domain: str
    size: Optional[str]=None; industry: Optional[str]=None; notes: Optional[str]=None
class Event(BaseModel):
    type: str; payload: dict = Field(default_factory=dict)
