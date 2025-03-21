from fastapi import APIRouter
from .do_stuff import do_stuff

router = APIRouter(prefix="/v1")

router.include_router(do_stuff.router)
