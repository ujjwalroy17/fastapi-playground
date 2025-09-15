from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel,Field
from typing import Annotated
app = FastAPI()

# application/x-www-form-urlencoded
# multipart/form-data

#HTML Form
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

# Pydantic models for forms    

# class FormData(BaseModel):
#     username : str
#     password : str

# pydantic models for forms with validations

class FormData(BaseModel):
    username : str = Field(min_length=3)
    password : str = Field(min_length=3,max_length=20)

@app.post("/login/")
async def login(Data : Annotated[FormData , Form()]):
    return Data
