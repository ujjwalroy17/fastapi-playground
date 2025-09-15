# 📌 FastAPI — Handling Form Data

## 🔹 Introduction
FastAPI normally works with **JSON** data for request bodies.  
But in web applications, data is often sent using **HTML forms**.  
To handle this, FastAPI provides the `Form()` dependency.  

This allows endpoints to **read form fields** from requests with content types:
- `application/x-www-form-urlencoded` → default for HTML forms  
- `multipart/form-data` → used when forms include files  

---

## 🚀 Serving an HTML Form
FastAPI can return a basic HTML form using `HTMLResponse`:

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
✔️ This serves a login form at /.

##  Receiving Form Data
We use Form() to tell FastAPI:
* **“This value should come from the form body, not from JSON or query parameters.”**

```python
from fastapi import Form
from typing import Annotated

@app.post("/login/")
async def login(
    username: Annotated[str, Form()], 
    password: Annotated[str, Form()]
):
    return {"username": username, "password_length": len(password)}
```
* Annotated[str, Form()] → means this parameter is a string that should come from the form.

* The username and password fields match the <input name=""> attributes in the HTML form.

## Adding Validation
We can add validation rules inside Form() (similar to Pydantic):

```python
@app.post("/login/")
async def login(
    username: Annotated[str, Form(min_length=3)], 
    password: Annotated[str, Form(min_length=3, max_length=20)]
):
    return {"username": username, "password_length": len(password)}
```
* min_length=3 → username and password must be at least 3 characters.

* max_length=20 → password must not exceed 20 characters.

* If the input fails, FastAPI automatically returns a 422 Unprocessable Entity error.

## Key Concepts Learned
##### 1. Form()
* Extracts values from HTML forms.

* Works only with application/x-www-form-urlencoded and multipart/form-data.

##### 2. HTMLResponse
* Allows returning raw HTML from endpoints (instead of JSON).

##### 3. Validation with Form()
* Can apply min_length, max_length, etc. directly inside the form definition.

##### 4. Difference from JSON
* Form() is for form submissions.

* Body() is for JSON data.

* Query() is for URL query parameters.


## 🔹 When to Use What

| Method   | Source              | Example Use              |
|----------|---------------------|--------------------------|
| `Query()` | URL query string    | Filters, search params   |
| `Body()`  | JSON body           | API requests (create/update) |
| `Form()`  | Form-data body      | Login forms, signup forms |
| `File()`  | Multipart form-data | File uploads             |


