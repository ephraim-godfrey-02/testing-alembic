from fastapi import APIRouter

route = APIRouter()

@route.get("/")
async def test_route():
    return {"message": "This is a test route"}
