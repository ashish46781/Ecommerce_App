from fastapi import FastAPI

app = FastAPI(title="E-Commerce API")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "E-Commerce API"}
