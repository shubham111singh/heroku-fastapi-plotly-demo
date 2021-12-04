from fastapi import FastAPI
from app.webservice.utils import NoUvicornException
from app.webservice.routes import root, collatz


# This app variable is used by uvicorn to serve the API.
app = FastAPI()

app.include_router(root.router)

app.include_router(
    collatz.router,
    prefix="/collatz",
    tags=["Collatz tag"],
)


# Display message when the webservice is invoked without uvicorn.
if __name__ == "__main__":
    raise NoUvicornException(port=5000)
