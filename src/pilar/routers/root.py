from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root() -> dict:
    """
    This is a GET endpoint for the root route of the Pilar API. It returns a
    dictionary containing a message indicating that the user has reached the
    root of the API and providing information on how to access the
    documentation.

    Returns:
        dict: A dictionary containing the root message.
    """

    return {
        "msg": "Root from Pilar. Access /docs or /redoc for more information.",
    }
