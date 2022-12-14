from typing import List


from pydantic import BaseModel, validator,ValidationError


class Model(BaseModel):
    values: List[int]

    @validator("values" ,pre = True)
    def split_string_values(cls, v):
        if isinstance(v, str):
            return v.split(",")
        return v


try :
    m = Model(values="1,2,3")
    print(m.values)  # [1, 2, 3]

except ValidationError as e:
    print(str(e) + "jjjjjj")


# i understand this feature