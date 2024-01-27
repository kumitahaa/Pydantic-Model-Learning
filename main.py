from model import Person


# Creating an Object based on the Pydantic Model with Fixed Data Types
# Can accept Email in EMAIL FORMAT only, and ID > 1
kumi = Person(name = "Kumi", email = "Kumi@gmail.com", id = 1)

print(f"Name: {kumi.name}    Email: {kumi.email}   ID: {kumi.id}")


# We create Object from a DICT as well

aabis_dict = {"name": "Aabis", "email": "aabis@gmail.com", "id": 2} # Dict with Data

aabis = Person(**aabis_dict) # Creating Object
# If there is wrong formatting in "aabis_dict", it will cause error right there.

print(f"Name: {aabis.name}    Email: {aabis.email}   ID: {aabis.id}")