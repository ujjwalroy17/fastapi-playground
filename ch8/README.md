# 📘 FastAPI – Path Converters

## 1. What are Path Converters?

In FastAPI, **path converters** allow you to capture more complex values from the URL path.  
Normally, path parameters only capture a **single segment** of the URL (until the next `/`).  
But sometimes, we need to capture an entire path (with `/` inside it).  

That’s where **path converters** come in.  

---

## 2. Example: Capturing a File Path

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {
        "your requested file at path" : file_path
    }
```
### How it works:

- `file_path:path` → the `:path` tells FastAPI to capture the **whole remaining path**, not just one segment.

**Example requests:**

- `/files/myfile.txt` → `"myfile.txt"`
- `/files/folder1/folder2/report.pdf` → `"folder1/folder2/report.pdf"`


## 3. Why Use Path Converters?
* To capture file paths from the URL.

* To work with nested resources (like folders, subfolders).

* Useful in cases like file systems, media files, or API versioning.

