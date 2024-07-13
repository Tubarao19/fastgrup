from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name= 'john'
    signup_ts: datetime | None = None
    friends: list[int] = []

#se pueden recibir estos datos desde el exterior

external_data = {
    'id':1234,
    'signup_ts': '2024-10-13 4:44',
    'friends': [10, 11, 12]
}

user = User(**external_data)
#los dos * ayudan a desestructurar los datos ingresados en user
# y complementarlos por los de external_data