import uvicorn

from fastapi import FastAPI

app = FastAPI()


class A:
    a = "original"


@app.get("/test")
def test():
    print(A.a)


if __name__ == "__main__":
    A.a = "changed"
    print(A.a)
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
    # uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    # uvicorn.run("main:app", host="127.0.0.1", port=8000, workers=4)
