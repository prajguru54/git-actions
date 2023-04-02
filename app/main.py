from fastapi import FastAPI

app = FastAPI()


def sum(a: int, b: int) -> int:
    return a + b


@app.get("/")
async def root():
    return {"message": "Hello Github Actions v0.5"}
