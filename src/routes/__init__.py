# Third Party Library
from fastapi import APIRouter

from routes.v1.films import router as films_router
# Project Stuff
from routes.v1.methods_router import router as methods_router
from routes.v1.person import router as person_router

# Init routers
router = APIRouter(prefix='/v1')
router.include_router(methods_router)
router.include_router(films_router)
router.include_router(person_router)
