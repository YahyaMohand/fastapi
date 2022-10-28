from typing import List
from datetime import date

from pydantic import BaseModel , validator,ValidationError,root_validator


# Applying validation at a field level
# class Model(BaseModel):
#     first_name : str
#     last_name : str
#     birthdate : date

#     @validator("birthdate")
#     def valid_birthdate(cls, v:date):
#         delta = date.today() - v
#         age = delta.days/365
#         if age > 120:
#             raise ValueError ("You seem a bit too old!")
#         return age



# try:
#     model = Model(
#         first_name = "yahya",
#         last_name = "mohand",
#         birthdate = "1997-01-19"
#     )
# except ValidationError as e:
#     print(str(e))
# print(model)


class User(BaseModel):
    name : str
    password : str
    password_confirm : str

    @root_validator()
    def password_check(cls, values):
        password = values.get("password")
        password_confirm = values.get("password_confirm")
        if password != password_confirm:
            raise ValueError ("dont match the pass")
        return values




try:
    user = User(
        name = "yahya",
        password = "123",
        password_confirm = "123"
    )
except ValidationError as e:
    print(str(e))

print(user)