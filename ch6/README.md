# 📘 FastAPI – Chapter 6: Path Parameters – Order Matters

## 1. Overview

In FastAPI, the **order of path operations matters**, especially when you have **static and dynamic paths** that could match similar URLs. This chapter explains why the order is important and what happens when paths are defined in different sequences.

---

## 2. FastAPI Setup

```
from fastapi import FastAPI

app = FastAPI()
```
---
## 3. Order Matters Example

## Static Path
```
@app.get("/product/roe_nt_usb")
async def single_product_static():
    return {"response": "Single Data Fetched"}
```

## Dynamic Path
```
@app.get("/product/{product_title}")
async def single_product_dynamic(product_title: str):
    return {"response": "Single Data Fetched", "product_title": product_title}
```
### What Happens:
#### Static path defined first:

* **/product/roe_nt_usb** matches the static route.

* **/product/any_other_title** matches the dynamic route.
✅ Works perfectly.

#### Dynamic path defined first (wrong order):

* **/product/roe_nt_usb** would match the dynamic route instead of the static one.

* The static route becomes unreachable.
❌ Causes unexpected behavior.

## 4. Key Concepts
### 4.1 Static Paths
* Paths with fixed URLs, e.g., /product/roe_nt_usb.

* Matched exactly as defined.

### 4.2 Dynamic Paths
* Paths with variables, e.g., /product/{product_title}.

* Can match multiple values.

### 4.3 Why Order Matters
* **FastAPI evaluates paths top to bottom.**

* **If a dynamic path comes before a static path, the dynamic route overrides the static one.**

* **Always define specific (static) routes first, then general (dynamic) routes.**
