from model import Person


# Creating an Object based on the Pydantic Model with Fixed Data Types
# Can accept Email in EMAIL FORMAT only, and ID > 1
kumi = Person(name = "Kumi", email = "Kumi@gmail.com", id = 1)

print(f"Name: {kumi.name}    Email: {kumi.email}   ID: {kumi.id}")