from a import A

import uvicorn

from fastapi import FastAPI

app = FastAPI()


@app.get("/test")
def test():
    print(A.a)


A.a = "changed"
print(A.a)
