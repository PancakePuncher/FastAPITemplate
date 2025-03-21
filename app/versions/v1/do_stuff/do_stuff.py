from fastapi import APIRouter


router = APIRouter(
    prefix="/do_stuff", tags=["Do Stuff Route Apart of the Version 1 Branch"]
)


@router.get("/do")
def do():
    return {"msg": "I'm doing stuff..."}
