# 📘 FastAPI – Multiple File Upload


## 🔹 Key Concepts

### 1. Multiple File Uploads
- FastAPI allows receiving **a list of files** from the client.  
- Files are sent using **`multipart/form-data`**.  
- In the HTML form, add the `multiple` attribute → `<input type="file" multiple>`.  
- In FastAPI, use a **list of `UploadFile`** to receive multiple files.  

---

### 2. Why `File()` with `UploadFile`?
- `File()` → tells FastAPI:  
  > “This data will come from `multipart/form-data` (file upload).”  
- `UploadFile` → the actual file object with properties like:  
  - `file.filename` → uploaded file name  
  - `file.content_type` → file type (e.g., `image/png`)  
  - `file.file` → file object (for reading/writing)  

✅ Together, they handle both **where data comes from** and **what type it is**.

---

### 3. Example Code

```python
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import Annotated
import os, shutil

app = FastAPI()

# HTML form for testing
@app.get("/", response_class=HTMLResponse)
async def main():
    return """
    <html>
        <body>
            <h2>Multiple File Upload (UploadFile)</h2>
            <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
                <input name="files" type="file" multiple>
                <input type="submit" value="Upload">
            </form>
        </body>
    </html>
    """

# Upload endpoint
@app.post("/uploadfiles/")
async def create_upload_file(files: Annotated[list[UploadFile], File()]):
    save_files = []
    os.makedirs("uploads", exist_ok=True)
    for file in files:
        save_path = f"uploads/{file.filename}"
        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        save_files.append({"filename": file.filename})
    return save_files
```
### 4. Explanation
* ```HTML Form:<input type="file multiple>``` allows selecting multiple files.

* Parameter: ```files:Annotated[list[UploadFile], File()]```
  * list[UploadFile] → multiple files are received as a list.

  * File() → ensures FastAPI looks in the file upload body.

* Saving files: Iterating over each file and writing to uploads/ folder.

* Response: Returns filenames of all uploaded files.

### 5. Handling Edge Cases
* No files uploaded → return empty list.

* Duplicate filenames → may overwrite files unless you handle renaming.

* Large files → use UploadFile (streaming) to avoid memory issues.

* Security → validate allowed file types (e.g., only .jpg, .pdf).



✅ Key Takeaways
* Use list[UploadFile] with File() for multiple uploads.

* All files are received via multipart/form-data.

* Iterate and save each file safely.

* Ideal for use cases like uploading documents, images, zip files, bulk uploads.