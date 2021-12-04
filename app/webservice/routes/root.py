from fastapi import APIRouter
from starlette.responses import RedirectResponse


router = APIRouter()


@router.get("/", include_in_schema=False)
def redirect_to_docs():
    """Redirect root directory to API docs
    """
    return RedirectResponse(url="/docs")
