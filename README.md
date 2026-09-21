# FastAPI Contact API

A beginner-friendly REST API built with **FastAPI** and **Pydantic** to manage contact information using CRUD operations.

The API includes **input validation** to ensure that contact details follow the required format before they are accepted.

## 🚀 Project Overview

This project demonstrates how to build a REST API using Python and FastAPI.

The API allows users to:

* Create a new contact
* View all contacts
* View a contact by ID
* Update an existing contact
* Delete a contact
* Validate user input before processing it

The project currently uses **in-memory storage**, so the data is available only while the FastAPI application is running.

---

## 🛠️ Technologies Used

* **Python**
* **FastAPI**
* **Pydantic**
* **Uvicorn**
* **Email Validator**
* **Swagger UI**

---

## 📁 Project Structure

```text
fastapi-contact-api/
│
├── main.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

### File Description

| File               | Purpose                                                                 |
| ------------------ | ----------------------------------------------------------------------- |
| `main.py`          | Contains the FastAPI application, CRUD operations, and validation logic |
| `requirements.txt` | Lists the Python packages required to run the project                   |
| `.gitignore`       | Specifies files and folders that should not be uploaded                 |
| `LICENSE`          | MIT License for the project                                             |
| `README.md`        | Project documentation                                                   |

---

# ✅ Input Validation

The API validates contact information using **Pydantic** before accepting the request.

If the user enters invalid information, FastAPI returns a **422 Validation Error** and the contact is not created or updated.

## 1. First Name

The first name must contain:

* Lowercase English letters only
* No numbers
* No spaces
* No special characters

### Valid

```text
gayathri
john
alex
```

### Invalid

```text
Gayathri
GAYATHRI
gayathri123
gayathri@
gayathri_kumar
gayathri kumar
```

Validation pattern:

```python
r"^[a-z]+$"
```

---

## 2. Last Name

The last name follows the same validation rule.

It must contain:

* Lowercase English letters only
* No numbers
* No spaces
* No special characters

### Valid

```text
kumar
smith
johnson
```

### Invalid

```text
Kumar
kumar123
kumar@
kumar_s
kumar raj
```

Validation pattern:

```python
r"^[a-z]+$"
```

---

## 3. Email

The email address is validated using Pydantic's `EmailStr`.

### Valid

```text
gayathri@gmail.com
john.smith@yahoo.com
user123@company.com
```

### Invalid

```text
gayathri@gmail
gayathri.com
@gmai.com
gayathri@
```

The `email-validator` package is required for email validation.

---

## 4. Contact Number

The contact number must contain **numbers only**.

No:

* Letters
* Spaces
* Hyphens
* Plus signs
* Special characters

### Valid

```text
9876543210
1234567890
```

### Invalid

```text
98765abc10
98765-43210
+919876543210
98765 43210
98765@43210
```

Validation pattern:

```python
r"^[0-9]+$"
```

> Note: This validation checks that the contact number contains digits only. It does not currently enforce a specific length such as exactly 10 digits.

---

# 🔄 CRUD Operations

CRUD stands for:

* **Create**
* **Read**
* **Update**
* **Delete**

## API Endpoints

| Method   | Endpoint                 | Description          |
| -------- | ------------------------ | -------------------- |
| `POST`   | `/contacts`              | Create a new contact |
| `GET`    | `/contacts`              | Get all contacts     |
| `GET`    | `/contacts/{contact_id}` | Get a contact by ID  |
| `PUT`    | `/contacts/{contact_id}` | Update a contact     |
| `DELETE` | `/contacts/{contact_id}` | Delete a contact     |

---

# 🟢 Create Contact

### Endpoint

```text
POST /contacts
```

### Request

```json
{
    "first_name": "gayathri",
    "last_name": "kumar",
    "email": "gayathri@gmail.com",
    "contact_number": "9876543210"
}
```

### Example Response

```json
{
    "message": "Contact created successfully",
    "contact": {
        "id": 1,
        "first_name": "gayathri",
        "last_name": "kumar",
        "email": "gayathri@gmail.com",
        "contact_number": "9876543210"
    }
}
```

The API automatically generates a unique ID for each contact.

---

# 🔵 Get All Contacts

### Endpoint

```text
GET /contacts
```

Returns all contacts stored in the application.

Example:

```json
[
    {
        "id": 1,
        "first_name": "gayathri",
        "last_name": "kumar",
        "email": "gayathri@gmail.com",
        "contact_number": "9876543210"
    },
    {
        "id": 2,
        "first_name": "john",
        "last_name": "smith",
        "email": "john@gmail.com",
        "contact_number": "9876543211"
    }
]
```

---

# 🔎 Get Contact by ID

### Endpoint

```text
GET /contacts/{contact_id}
```

Example:

```text
GET /contacts/1
```

Returns the contact with ID `1`.

If the ID does not exist, the API returns:

```json
{
    "detail": "Contact not found"
}
```

with HTTP status code:

```text
404 Not Found
```

---

# 🟡 Update Contact

### Endpoint

```text
PUT /contacts/{contact_id}
```

Example:

```text
PUT /contacts/1
```

### Request

```json
{
    "first_name": "gayathri",
    "last_name": "sharma",
    "email": "gayathri.sharma@gmail.com",
    "contact_number": "9876543212"
}
```

The same validation rules are applied during an update.

If invalid information is entered, the update is rejected.

---

# 🔴 Delete Contact

### Endpoint

```text
DELETE /contacts/{contact_id}
```

Example:

```text
DELETE /contacts/1
```

If the contact exists, it is removed from the list.

Example response:

```json
{
    "message": "Contact deleted successfully"
}
```

If the ID does not exist:

```json
{
    "detail": "Contact not found"
}
```

---

# 📖 Swagger API Documentation

FastAPI automatically provides interactive API documentation using Swagger UI.

When running locally, open:

```text
http://127.0.0.1:8000/docs
```

Swagger allows you to:

* View all API endpoints
* Enter request data
* Test POST, GET, PUT, and DELETE operations
* Test input validation
* View API responses
* Check HTTP status codes

After deployment, the same Swagger documentation can be accessed using your public API URL followed by:

```text
/docs
```

---

# ⚙️ Installation and Setup

## 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

Move into the project directory:

```bash
cd fastapi-contact-api
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Run the Application

```bash
python -m uvicorn main:app --reload
```

The application will start locally.

Open the Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 📦 Requirements

The project uses the following main dependencies:

```text
fastapi
uvicorn
pydantic
email-validator
```

---

# 🔐 Error Handling

The API handles invalid requests using FastAPI and Pydantic validation.

For invalid input, FastAPI returns:

```text
422 Unprocessable Entity
```

For requests involving a contact ID that does not exist, the API returns:

```text
404 Not Found
```

Example:

```json
{
    "detail": "Contact not found"
}
```

---

# 💾 Data Storage

This project currently uses a Python list for storing contacts.

```python
contacts = []
```

Therefore:

* Data is stored in memory
* Data is not permanently saved
* Restarting the application clears the contacts
* IDs start again when the application restarts

A future version can use a database such as **SQLite** or **PostgreSQL** for persistent storage.

---

# 🎯 Learning Objectives

This project was created to understand:

* REST API fundamentals
* FastAPI application structure
* HTTP methods
* CRUD operations
* Request and response handling
* Pydantic data validation
* Regular expressions for input validation
* HTTP status codes
* Error handling
* Swagger API documentation
* API deployment

---

# 🚀 Future Improvements

Possible improvements include:

* Add SQLite/PostgreSQL database
* Use a real database primary key
* Add authentication and authorization
* Add pagination
* Add search and filtering
* Add stronger contact-number validation
* Add automated tests using Pytest
* Add Docker support
* Add environment variables for configuration
* Improve API error responses

---

## 👩‍💻 Project

**FastAPI Contact API**

A simple REST API demonstrating CRUD operations and input validation using FastAPI and Pydantic.
