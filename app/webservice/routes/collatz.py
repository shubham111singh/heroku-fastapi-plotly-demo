from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from app.logic.collatz import collatz_sequence, collatz_graph
from typing import List


router = APIRouter()


# Create route from existing function without modification
router.get("/sequence/{x}")(
    collatz_sequence
)


@router.get("/graph/{x_cslist}", response_class=HTMLResponse)
def collatz_graph_from_list(x_cslist: str) -> str:
    """Collatz plots for an integer or a comma-separated list of integers
    """

    # Parse the string into an int list
    python_list = [int(x0) for x0 in x_cslist.split(",")]
    # QUESTION: Can we do this better? We could at least use
    # a decorator...

    return collatz_graph(python_list)
