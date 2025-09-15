# 📘 FastAPI – Single File Upload

## 🔹 Key Concepts

### 1. File Upload in FastAPI
- FastAPI supports file uploads through the `File()` dependency.  
- Files are sent using **`multipart/form-data`**, not JSON.  
- HTML forms with `<input type="file">` can be used for testing uploads.  

---

### 2. `File` vs `UploadFile`
| Feature       | `File` (Dependency)                           | `UploadFile` (Data Type) |
|---------------|-----------------------------------------------|---------------------------|
| Purpose       | Tells FastAPI the data comes from a file upload (`multipart/form-data`) | Represents the uploaded file object |
| Data handling | Without it, FastAPI assumes JSON, not file data | Provides `.filename`, `.content_type`, `.file` |
| Memory usage  | Stores entire file in memory (if used directly) | Efficient, streams large files |
| Use case      | Must be used with `UploadFile` to indicate source | Best for accessing and saving uploaded files |

 **Why both?**  
- `File()` → **where data comes from** (form-data file field).  
- `UploadFile` → **what type of object** (the actual uploaded file).  

---

### 3. Example Code

```python
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import Annotated
import os, shutil

app = FastAPI()

# HTML Form for testing
@app.get("/", response_class=HTMLResponse)
async def main():
    return """
    <html>
        <body>
            <h2>Single File Upload (UploadFile)</h2>
            <form action="/uploadfile/" enctype="multipart/form-data" method="post">
                <input name="file" type="file">
                <input type="submit" value="Upload">
            </form>
        </body>
    </html>
    """

# Upload endpoint
@app.post("/uploadfile/")
async def create_upload_file(file: Annotated[UploadFile | None, File()] = None):
    if not file:
        return {"message": "No upload file sent"}
    
    save_path = f"uploads/{file.filename}"
    os.makedirs("uploads", exist_ok=True)
    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return {
        "filename": file.filename,
        "content_type": file.content_type
    }
```
### 4. Explanation
* `File()`: Dependency that tells FastAPI the data is coming from multipart/form-data.

* `UploadFile`: Provides access to file properties and file object.

* `Saving file`: Used shutil.copyfileobj() for efficient writing.

* `Folder creation`: os.makedirs("uploads", exist_ok=True) ensures folder exists.

### 5. Handling Edge Cases
* No file uploaded → return a message.

* Large files → prefer UploadFile to avoid memory issues.

* Security tip → validate file type/extension before saving.



### Key Takeaways
* Use UploadFile with File() for safe & efficient file uploads.

* Files are received as multipart/form-data.

* File() tells FastAPI the source, UploadFile gives the object.

* Useful for features like profile picture uploads, document submission, image galleries, etc.