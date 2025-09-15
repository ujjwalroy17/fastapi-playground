# 📌 FastAPI — Form Data with Pydantic Model

## 🔹 Introduction
In FastAPI, you can handle **HTML form submissions** using `Form()` and **validate data** using **Pydantic models**.  

This approach is useful when you want:
- Structured data from forms.
- Validation rules on form inputs.
- Clean and maintainable endpoints.

HTML forms typically send data using content types:
- `application/x-www-form-urlencoded` → default for forms without files.  
- `multipart/form-data` → for forms including files.

---

## 🚀 Serving an HTML Form
You can return a simple HTML form using `HTMLResponse`:

```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def get_form():
    return """
    <html>
        <body>
            <h2>Login Form</h2>
            <form action="/login/" method="post">
                <label for="username">Username:</label><br>
                <input type="text" id="username" name="username"><br>
                <label for="password">Password:</label><br>
                <input type="password" id="password" name="password"><br><br>
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
    """
```
*  This will serve a login form at /.

## Handling Form Data with Pydantic
### 1️⃣ Basic Pydantic Model
You can define a Pydantic model to represent form data:

```python
from pydantic import BaseModel

class FormData(BaseModel):
    username: str
    password: str
```
* Each field corresponds to a form input (name attribute in HTML).

* FastAPI can then receive the form data as an instance of this model.

### 2️⃣ Adding Validation
You can also add validation rules using Field():

```python
from pydantic import Field

class FormData(BaseModel):
    username: str = Field(min_length=3)
    password: str = Field(min_length=3, max_length=20)
```
* min_length → minimum number of characters.

* max_length → maximum number of characters.

* FastAPI automatically returns 422 Unprocessable Entity if validation fails.

### 3️⃣ Receiving Form Data in Endpoint
```python
from fastapi import Form
from typing import Annotated

@app.post("/login/")
async def login(Data: Annotated[FormData, Form()]):
    return Data
```
* Annotated[FormData, Form()] → tells FastAPI:

  * “Take each field of FormData from form-data, not JSON.”

* Each input field in the HTML form (username, password) is mapped to the Pydantic model fields.

## Key Concepts Learned
#### 1.Form()

* Extracts form-data values.

* Supports application/x-www-form-urlencoded and multipart/form-data.

#### 2.Pydantic Model + Field

* Defines structured form data.

* Adds validation rules directly on fields.

* Annotated[Model, Form()]

* Maps Pydantic model fields to form-data parameters.
