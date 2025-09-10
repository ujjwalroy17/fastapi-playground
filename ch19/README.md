# 🍪 FastAPI – Cookie Parameters

## 1. What are Cookies?
- A **cookie** is like a small note stored in your browser.  
- Websites use cookies to remember things like:
  - Who you are (session/login info)  
  - Preferences (dark mode, language)  
  - Shopping cart items  

👉 When you revisit a site, your browser **automatically sends the cookie back** to the server.

---

## 2. Cookie Parameters in FastAPI
In FastAPI, we can access cookies from requests using the `Cookie()` function.  
Let’s see an example:

```python
from fastapi import FastAPI, Cookie
from typing import Annotated

app = FastAPI()

@app.get("/products/recommendations")
async def get_recommendations(session_id: Annotated[str | None, Cookie()] = None):
    if session_id:
        return {"message": f"Recommendations for session {session_id}", "session_id": session_id}
    else:
        return {"message": "No session_id provided, showing default recommendations"}
```
## 3. How it works:
* session_id : Annotated[str | None, Cookie()] = None

    * Tells FastAPI: “Look for a cookie named session_id”.

    * It can be a string (str) or None if not found.

### Example Scenarios
#### Case 1: Cookie present
```
Cookie: session_id=abc123
```

✅ Response:

```
{
  "message": "Recommendations for session abc123",
  "session_id": "abc123"
}
```
#### Case 2: Cookie missing

```
(no session_id cookie)
```
```
{
  "message": "No session_id provided, showing default recommendations"
}
```
### 4. Why use Cookie Parameters?
✅ Automatic → browser sends cookies without user typing them

✅ Useful for sessions → track logged-in users

✅ Cleaner URLs → no need to pass data in path/query params

✅ Personalization → recommendations, preferences, etc.

