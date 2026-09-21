from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()



class Contact(BaseModel):
    first_name: str = Field(
        pattern=r"^[a-z]+$"
    )

    last_name: str = Field(
        pattern=r"^[a-z]+$"
    )

    email: EmailStr

    contact_number: str = Field(
        pattern=r"^[0-9]+$"
    )

contacts = []
next_id = 1


@app.get("/")
def home():
    return {"message": "Contact API is running"}


# CREATE
@app.post("/contacts")
def create_contact(contact: Contact):
    global next_id

    new_contact = {
        "id": next_id,
        "first_name": contact.first_name,
        "last_name": contact.last_name,
        "email": contact.email,
        "contact_number": contact.contact_number
    }

    contacts.append(new_contact)
    next_id += 1

    return {
        "message": "Contact created successfully",
        "contact": new_contact
    }


# READ ALL
@app.get("/contacts")
def get_contacts():
    return contacts


# READ ONE
@app.get("/contacts/{contact_id}")
def get_contact(contact_id: int):

    for contact in contacts:
        if contact["id"] == contact_id:
            return contact

    raise HTTPException(status_code=404, detail="Contact not found")

# UPDATE
@app.put("/contacts/{contact_id}")
def update_contact(contact_id: int, contact: Contact):

    for existing_contact in contacts:
        if existing_contact["id"] == contact_id:

            existing_contact["first_name"] = contact.first_name
            existing_contact["last_name"] = contact.last_name
            existing_contact["email"] = contact.email
            existing_contact["contact_number"] = contact.contact_number

            return {
                "message": "Contact updated successfully",
                "contact": existing_contact
            }

    raise HTTPException(status_code=404, detail="Contact not found")

# DELETE
@app.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int):

    for contact in contacts:
        if contact["id"] == contact_id:

            contacts.remove(contact)

            return {
                "message": "Contact deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Contact not found"
    )