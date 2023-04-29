from pydantic import BaseModel, EmailStr
from .. import *


class User(BaseModel):
    userAddress: str
    userRole: str
    email: EmailStr
    isApproved: bool = False
