# Third Party Library
from fastapi import APIRouter

# Project Stuff
from routes.v1.methods_router import router as methods_router

# Init routers
router = APIRouter(prefix='/v1')
router.include_router(methods_router)