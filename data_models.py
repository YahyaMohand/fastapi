from datetime import date
from email.policy import default
from enum import Enum
from typing import List, Optional
from xml.etree.ElementInclude import include

from pydantic import BaseModel, ValidationError, Field,EmailStr,HttpUrl



def list_factory():
    return ['a','b','c']


class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    NON_BINARY = "NON_BINARY"


class Address(BaseModel):
    street_address: str
    postal_code: str
    # city: str
    city : str = Field(...,min_length = 3)
    country: Optional[str] = None
    url : HttpUrl


class Person(BaseModel):
    first_name: str
    last_name: str
    E_mail : EmailStr
    gender: Gender
    birthdate: date
    interests: List[str]
    address: Address


# Invalid address
# try:
#     Person(
#         first_name="John",
#         last_name="Doe",
#         gender=Gender.MALE,
#         birthdate="1991-01-01",
#         interests=["travel", "sports"],
#         address={
#             "street_address": "12 Squirell Street",
#             "postal_code": "424242",
#             "city": "Woodtown",
#             # Missing country
#         },
#     )
# except ValidationError as e:
#     print(str(e))

# Valid
try:
    person = Person(
    first_name="John",
    last_name="Doe",
    E_mail="yhaya@kjsdns.cpkc",
    gender=Gender.MALE,
    birthdate="1991-01-01",
    interests=["travel", "sports",'jjxs'],
    address={
        "street_address": "12 Squirell Street",
        "postal_code": "424242",
        "city": "Mosul",
        "url" :"http://www.ksdmck.lll"
        # "country": "US", // possible add this value if dont used return None value.
    },
)
except ValidationError as e:
    print(str(e))


# Working with Pydantic objects
print(person.dict() )
print(',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,')
print(person.dict(include={
    'first_name',
    'last_name',
 }))

print(',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,')


print(person.dict(exclude={'first_name','address'}))


