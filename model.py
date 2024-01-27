from pydantic import BaseModel, EmailStr, validator

# Pydantic is a Type Validtion Module for python
# Python has dynamic type for variables, We can change  the type of variable during execution as well
# Pydantic provides a structure in which we can Fix the Data Types

class Person(BaseModel):
    name: str
    email: EmailStr #Email String (Will cause Error if not including @ sign)
    id: int

    @validator("id") # Custom Type Validation

    def validate_id(cls, value):
        if value >= 0:
            return value
        else:
            raise ValueError(f"id cannot be negative.")