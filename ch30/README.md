# 📘 FastAPI – Form Field and File Upload Together


## 🔹 Key Concepts

### 1. Mixing Form Fields and Files
- FastAPI allows sending both **form fields** (like username, email, etc.) and **file uploads** in the same request.  
- Both must use `enctype="multipart/form-data"` in the HTML form.  
- Use `Form()` for text fields and `File()` with `UploadFile` for file uploads.

---

### 2. Why Form() + File()?
- **`Form()`** → tells FastAPI to read the value from form-data text fields.  
- **`File()`** → tells FastAPI to read the value from uploaded files.  
- **`UploadFile`** → provides file details (`filename`, `content_type`, `file`).  

✅ Together, this allows APIs like **user profile creation with profile picture**.

---

### 3. Example Code

```python
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from typing import Annotated
import os, shutil

app = FastAPI()

# HTML form
@app.get("/", response_class=HTMLResponse)
async def get_form():
    return """
    <html>
        <head>
            <title>User Profile Upload</title>
        </head>
        <body>
            <h2>User Profile Form</h2>
            <form action="/user-with-file/" enctype="multipart/form-data" method="post">
                <label for="username">Username:</label><br>
                <input type="text" id="username" name="username" required><br><br>
                <label for="file">Profile Picture (optional):</label><br>
                <input type="file" id="file" name="file" accept="image/*"><br><br>
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
    """

# API endpoint
@app.post("/user-with-file/")
async def create_user_with_file(
    username: Annotated[str, Form()],
    file: Annotated[UploadFile | None, File()] = None
):
    response = {"username": username}
    if file:
        save_path = f"uploads/{file.filename}"
        os.makedirs("uploads", exist_ok=True)
        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        response["filename"] = file.filename
    return response
```
### 4. Explanation
* Form field: ```username: Annotated[str, Form()]``` → text input.

* File field: ```file: Annotated[UploadFile | None, File()] ```→ optional profile picture.

* Multipart encoding: Required since we are mixing text + files.

* Saving file: Stores the uploaded file inside the uploads/ directory.

* Response: Returns username and filename (if uploaded).

### 5. Handling Edge Cases
* File field is optional (UploadFile | None).

* Large files handled efficiently via UploadFile.

* Validate allowed file types using file.content_type or extension.

* Prevent overwriting by renaming files (e.g., add timestamp/UUID).

### Key Takeaways
* Use Form() for text and File() with UploadFile for files in the same request.

* Requires multipart/form-data encoding.

* Ideal for features like user profile creation, resumes with details, product uploads with description.


